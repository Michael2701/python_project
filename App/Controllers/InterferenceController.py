""" File describe Interference controller.

Interference this output data of our tool.
"""

import subprocess
from typing import Any

from App.Controllers.Controller import Controller
from App.Models.InterferenceModel import InterferenceModel
from App.Models.InterferenceRowModel import InterferenceRowModel
from App.Views.InterferenceView import InterferenceView

from App.Models.SQLiteConnector import SQLiteConnector
from App.Services.Message import Message


class InterferenceController(Controller):
    def __init__(self, master: Any = None):
        self.get_logged_user()
        self.master = master
        self.msg = Message

    def create_interference(self, file: InterferenceRowModel, data: dict):
        subprocess.check_call([r"App/Services/c/InterferenceCalculator", "App/triplet_of_genes.csv", "Interference.csv", str(file.id), str(data["step"]), str(data["min_distance"]), str(data["max_distance"])])

    def show_interference_view(self) -> None:
        """
        call to interference view and show user research according user status (user/admin)
        :return: None
        """
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

    def open_file_process_modal(self, f, param) -> None:
        """
        this function will be implemented in future versions.
        :param f: Genetic file
        :param param: parameters
        :return: None
        """
        pass

    def show_delete_modal(self, file: tuple) -> None:
        """
        show delete modal
        :param file: GeneticFileModel object
        :return: None
        """
        if self.msg.question("Do you really want to delete this file?", "Delete File"):
            self.delete_file(file[0])

    def delete_file(self, file_id: int) -> bool:
        """
        delete file with given file id
        :param file_id: id of file to delete
        :return: True if file deleted and False otherwise
        """
        try:
            InterferenceModel.delete(str(file_id))
            self.show_interference_view()
            return True
        except Exception as e:
            print(str(e))
            self.msg.warning("Warning. File not deleted")
            return False
