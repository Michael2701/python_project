""" File describe Interference controller.

Interference this output data of our tool.
"""
import os
import subprocess
from datetime import datetime
from os import path
from typing import Any

import xlsxwriter

from App.Controllers.Controller import Controller
from App.Models.InterferenceModel import InterferenceModel
from App.Models.InterferenceRowModel import InterferenceRowModel
from App.Models.SQLiteConnector import SQLiteConnector
from App.Services.GraphCreator import GraphCreator
from App.Services.Message import Message
from App.Views.InterferenceView import InterferenceView
from App.Views.UIElements.GraphModal import GraphModal


class InterferenceController(Controller):
    def __init__(self, master: Any = None):
        self.get_logged_user()
        self.master = master
        self.msg = Message

    def create_interference(self, file: InterferenceRowModel, data: dict):
        subprocess.check_call(
            [r"App/Services/c/InterferenceCalculator", "App/triplet_of_genes.csv", "Interference.csv", str(file.id),
             str(data["step"]), str(data["min_distance"]), str(data["max_distance"])])

    def create_interference_excel(self, file: tuple) -> None:
        """
        create file and write to it interference calculations
        :return: None
        """
        if self.__create_folder_for_interference_excel():
            time_stamp = datetime.now()
            date_time = time_stamp.strftime("%d-%m-%Y_%H:%M")

            workbook = xlsxwriter.Workbook(self.dir_user_research_path +
                                           '/' + date_time + '_' +
                                           self.user['first_name'] + '.xlsx')
            worksheet = workbook.add_worksheet()

            self.__write_title_to_excel(worksheet)

            row = 1
            for line in self.__get_interference_rows(file):
                col = 0

                for word in line:
                    if isinstance(word, str):
                        word = word.replace('\n', '')

                    worksheet.write(row, col, word)
                    col += 1
                row += 1

            workbook.close()

    def __write_title_to_excel(self, worksheet: Any) -> None:
        titles = (
                'id', 'interference_id', 'marker 1', 'marker 2', 'marker 3',
                'r1', 'r2', 'N_00', 'N_01', 'N_10', 'N_11', 'C max', 'log(C max)', 'log(C=1)', 'Xi')
        row = 0
        for title in titles:
            worksheet.write(0, row, title)
            row += 1

    def __get_interference_rows(self, interference: tuple) -> list:
        """
        pull interference rows from database
        :param interference:
        :return: rows - list of rows
        """
        connection = SQLiteConnector.create_connection('App/DB/project.db')
        cur = connection.cursor()
        cur.execute("SELECT * FROM interference_row where interference_id=" + str(interference[0]))

        rows = cur.fetchall()
        return rows

    def __create_folder_for_interference_excel(self) -> bool:
        """
        create main folder for all researches (interference excel files) and private user folder
        :return: True if all needed folders exists or created now otherwise False
        """
        user = Controller().get_logged_user()
        dir_research_path = "App/../Researches"
        self.dir_user_research_path = dir_research_path + '/' + user['first_name'] + ' ' + user['last_name']

        if not path.exists(dir_research_path):
            try:
                os.mkdir(dir_research_path)
            except OSError:
                print("Can't create \"Researches\" directory")

        if not path.exists(self.dir_user_research_path):
            try:
                os.mkdir(self.dir_user_research_path)
            except OSError:
                print("Can't create user directory in \"Researches\" directory")

        return path.exists(dir_research_path) and path.exists(self.dir_user_research_path)

    def create_interference_graph(self, file: tuple) -> None:
        """

        :param file:
        :return:
        """
        GraphModal(self.master, self.__get_interference_rows(file))
        # graph = GraphCreator(self.__get_interference_rows(file))
        # graph.create()

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
            cur.execute(
                f"select i.*, f.file_name name from interference i LEFT JOIN files f ON i.file_id=f.id WHERE f.user_id IN ({user_file_ids})")

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
