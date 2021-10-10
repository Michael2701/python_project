import subprocess
from typing import Any

from App.Controllers.Controller import Controller
from App.Models.InterferenceRowModel import IntereferenceRowModel
from App.Models.SQLiteConnector import SQLiteConnector
from App.Views.InterferenceView import InterferenceView


class InterferenceController(Controller):
    def __init__(self, master: Any = None):
        self.get_logged_user()
        self.master = master

    def create_interference(self, file: IntereferenceRowModel, data: dict):
        subprocess.check_call([r"App/Services/c/InterferenceCalculator", "App/triplet_of_genes.csv", "Interference.csv", str(file.id), str(data["step"]), str(data["min_distance"]), str(data["max_distance"])])

    def show_interference_view(self):
        self.clear_view(self.master)
        connection = SQLiteConnector.create_connection('App/DB/project.db')
        cur = connection.cursor()
        cur.execute("select i.*, f.file_name name from interference i LEFT JOIN files f ON i.file_id=f.id")

        if self.user['user_role'] == 'admin':
            cur.execute("select i.*, f.file_name name from interference i LEFT JOIN files f ON i.file_id=f.id")
        else:
            user_file_ids = ",".join(cur.execute(f"SELECT id FROM WHERE user_id={self.user.id}"))
            cur.execute(f"select i.*, f.file_name name from interference i LEFT JOIN files f ON i.file_id=f.id WHERE f.user_id IN ({user_file_ids})")

        files = cur.fetchall()
        InterferenceView(self, self.master, files)
