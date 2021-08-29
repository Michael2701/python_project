import subprocess
from typing import Any

from App.Controllers.Controller import Controller
from App.Models.TripletMarkersCalc import TripletMarkersCalc
# from App.Views.InterferenceView import InterferenceView
from App.Models.SQLiteConnector import SQLiteConnector


class InterferenceController(Controller):
    def __init__(self, master: Any = None):
        self.get_logged_user()
        self.master = master

    def create_interference(self, file: TripletMarkersCalc, data: dict):
        subprocess.check_call([r"App/Services/c/InterferenceCalculator", "App/triplet_of_genes.csv", "Interference.csv", str(file.id), str(data["step"]), str(data["min_distance"]), str(data["max_distance"])])

    def show_interference_view(self):
        print('here')
        print(self.user)
        connection = SQLiteConnector.create_connection('App/DB/project.db')
        cur = connection.cursor()
        cur.execute("select * from markers_calc")
        print(cur.fetchall())

        # if self.user['user_role'] == 'admin':
        #     print(self.user)
        #     files = TripletMarkersCalc.select(" file_id > 0")
        #     for file in files:
        #         print(file.id)
        # else:
        #     files = TripletMarkersCalc.select(TripletMarkersCalc.q.user_id == self.user['id'])
        # InterferenceView(self, self.master, files)
