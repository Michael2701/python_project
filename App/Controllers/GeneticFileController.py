from datetime import datetime
from tkinter import *
from typing import Any

import xlsxwriter as xlsxwriter

from App.Services.FileUploader import FileUploader
from App.Services.Message import Message
from App.Controllers.Controller import Controller

from App.Models.GeneticFileModel import GeneticFileModel
from App.Views.GeneticFilesView import GeneticFilesView
from App.Views.UIElements.FileProcessModal import FileProcessModal

from App.Views.UIElements.UpdateFileMetaModal import UpdateFileMetaModal
from App.Views.UIElements.FileUploadModal import FileUploadModal
from App.Models.GeneModel import GeneModel


class GeneticFileController(Controller):
    keys_list = ['AAA', 'AAB', 'AAH', 'ABA', 'ABB', 'ABH', 'AHA', 'AHB', 'AHH',
                 'BAA', 'BAB', 'BAH', 'BBA', 'BBB', 'BBH', 'BHA', 'BHB', 'BHH',
                 'HAA', 'HAB', 'HAH', "HBA", "HBB", 'HBH', 'HHA', 'HHB', 'HHH']

    def __init__(self, master: Any = None) -> None:
        """
        :param master: parent view
        """
        self.top_level_dialog = UpdateFileMetaModal(master, self)
        self.file_process_dialog = FileProcessModal(master, self)
        self.get_logged_user()
        self.msg = Message
        self.master = master
        self.notebook = None
        self.result_markers = []

    def display_files(self) -> None:
        """
        display all files as a table
        :return:
        """
        self.clear_view(self.master)
        if self.user['user_role'] == 'admin':
            files = GeneticFileModel.select('id > 0')
        else:
            files = GeneticFileModel.select(GeneticFileModel.q.user_id == self.user['id'])
        self.notebook = GeneticFilesView(self, self.master, files)

    def show_delete_modal(self, file: GeneticFileModel) -> None:
        """
        show delete modal
        :param file: GeneticFileModel object
        :return: None
        """
        if self.msg.question("Do you really want to delete this file?", "Delete File"):
            self.delete_file(file.id)

    def show_update_file_modal(self, file=None):
        """
        show file update modal
        :param file: None or GeneticFileModel object
        :return: None
        """
        self.top_level_dialog.show_top_level_dialog(file)

    def update_file(self, file: GeneticFileModel, data: dict) -> None:
        """
        update file data
        :param file: GeneticFileModel object
        :param data: dictionary with new data to save in given object
        :return: None
        """
        try:
            file.set(
                user_id=data['user_id'],
                file_name=data['file_name'],
                file_description=data['file_description'],
                file_created_at=data['file_created_at']
            )
            self.display_files()
            self.msg.info("File updated")
        except Exception as e:
            print(str(e))
            self.msg.warning("Warning. File not updated")

    def upload_file(self) -> None:
        """
        show upload file modal
        :return: None
        """
        FileUploadModal(self, self.master)

    def create_file(self, data: dict) -> None:
        """
        create and save GeneticFileModel
        :param data: dictionary with data to save
        :return: None
        """
        try:
            genetic_file = GeneticFileModel(
                user_id=data['user_id'],
                file_name=data['file_name'],
                file_description=data['file_description'],
                file_created_at=data['file_created_at']
            )

            fu = FileUploader(data['file_path'], str(genetic_file.id))
            fu.upload_file()

            self.display_files()
            self.msg.info("File created")

        except Exception as e:
            print(str(e))
            self.msg.warning("Warning. File not created")

    def open_file_process_modal(self, file: GeneticFileModel, is_excel: bool):
        self.file_process_dialog.show_top_level_dialog(file, is_excel)

    def process_file_genes(self, data: dict) -> None:
        self.calculate_markers_genes(self.get_groups_of_markers(str(data["id"]), data))

    def calculate_markers_genes(self, gene_ids_groups) -> None:
        """
        :param gene_ids_groups:
        :return:
        """

        self.result_markers = []
        try:
            for gene_ids_group in gene_ids_groups:
                ids_string = ','.join([str(gene_id) for gene_id in gene_ids_group])
                in_group = 'id in (' + ids_string + ')'
                genes_data = GeneModel.select(in_group)
                genes_summary = {
                    "name": [],
                    "distance": [],
                    "successors": []
                }
                for gdata in genes_data:
                    successors_list = gdata.successors.split(',')
                    genes_summary["name"].append(gdata.name)
                    genes_summary["distance"].append(gdata.distance)
                    if not len(genes_summary["successors"]):
                        genes_summary["successors"] = successors_list
                    else:
                        for i, successor in enumerate(successors_list):
                            genes_summary["successors"][i] += successor

                result_dict = {}
                for s in genes_summary["successors"]:
                    if s in result_dict.keys():
                        result_dict[s] += 1
                    else:
                        result_dict[s] = 1

                self.result_markers.append({
                    "name": genes_summary["name"],
                    "distance": genes_summary["distance"],
                    "successors": result_dict
                })
        except Exception as e:
            self.msg.error("Error creating markers excel")
            print(e)

    def create_markers_statistic_excel(self) -> None:
        """
        Create .xlsx file of triples markers and add statistics to it
        :return: None
        """
        print("Log: In create_markers_statistic_excel()")
        now = datetime.now()
        date_time = now.strftime("%d-%m-%Y_%H:%M:%S")

        workbook = xlsxwriter.Workbook(self.user['first_name'] + "_" +
                                       self.user['last_name'] + "_" +
                                       date_time + '.xlsx')
        worksheet = workbook.add_worksheet()
        row = 0

        for lines in self.create_list_of_markers():
            col = 0
            for line in lines:
                worksheet.write(row, col, line)
                col += 1
            row += 1

        workbook.close()
        print("Log: Exit create_markers_statistic_excel()")

    def create_list_of_markers(self) -> list:
        """

        :return:
        """
        list_of_markers = []
        titles = ['marker 1', 'marker 2', 'marker 3', 'position 1', 'position 2', 'position 3']

        titles.extend(self.keys_list)
        list_of_markers.append(titles)

        for markers in self.result_markers:
            line = [name for name in markers['name']]
            line.extend(markers['distance'])
            for key in self.keys_list:
                if key in markers["successors"].keys():
                    line.append(markers["successors"][key])
                else:
                    line.append(0)
            list_of_markers.append(line)
        return list_of_markers

    def get_groups_of_markers(self, file_id: str, data: dict) -> list:
        """
        build group of three gene id's and return list of them
        :param file_id: file ID
        :param data:
        :return: list of triple id's
        """
        genes = [gene for gene in GeneModel.selectBy(file_id=file_id)]
        gene_ids_groups = []
        for i in range(0, len(genes), data["step"]):
            gene_ids = GeneModel.get_id_list(genes[i].id, str(data["id"]), data["min_distance"], data["max_distance"])
            if len(gene_ids) > 3:
                for x in range(len(gene_ids) - 2):
                    for y in range((x + 1), len(gene_ids) - 1):
                        for z in range((y + 1), len(gene_ids)):
                            gene_ids_groups.append([gene_ids[x], gene_ids[y], gene_ids[z]])
            elif len(gene_ids) == 3:
                gene_ids_groups.append(gene_ids)
        return gene_ids_groups

    def delete_file(self, file_id: int) -> bool:
        """
        delete file with given file id
        :param file_id: id of file to delete
        :return: True if file deleted and False otherwise
        """
        try:
            GeneticFileModel.delete(file_id)
            self.display_files()
            return True
        except Exception as e:
            print(str(e))
            self.msg.warning("Warning. File not deleted")
            return False

    def aaa(self):
        pass
