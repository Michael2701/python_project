from tkinter import *

from App.Services.Message import Message
from App.Controllers.Controller import Controller

from App.Models.GeneticFileModel import GeneticFileModel
from App.Views.GeneticFilesView import GeneticFilesView

from App.Views.UIElements.UpdateFileMetaModal import UpdateFileMetaModal
from App.Views.UIElements.FileUploadModal import FileUploadModal


class GeneticFileController(Controller):

    def __init__(self, master=None):
        self.top_level_dialog = UpdateFileMetaModal(master, self)
        self.msg = Message
        self.master = master
        self.notebook = None

    def display_files(self) -> None:
        self.clear_view(self.master)
        files = GeneticFileModel.select('id > 0')
        self.notebook = GeneticFilesView(self, self.master, files)

    def show_delete_modal(self, file: GeneticFileModel) -> None:
        if self.msg.question("Do you really want to delete this file?", "Delete File"):
            self.delete_file(file.id)

    def show_update_file_modal(self, file=None):
        self.top_level_dialog.show_toplevel_dialog(file)

    def update_file(self, file: GeneticFileModel, data: dict) -> None:
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
        FileUploadModal(self, self.master)

    def create_file(self, data: dict) -> None:
        try:
            genetic_file = GeneticFileModel(
                user_id=data['user_id'],
                file_name=data['file_name'],
                file_description=data['file_description'],
                file_created_at=data['file_created_at']
            )

            print(genetic_file.id)
            file_id = genetic_file.id

            self.display_files()
            self.msg.info("File created")

        except Exception as e:
            print(str(e))
            self.msg.warning("Warning. File not created")

    def delete_file(self, id: int):
        try:
            GeneticFileModel.delete(id)
            self.display_files()
            self.msg.info("File deleted")
            return True
        except Exception as e:
            print(str(e))
            self.msg.warning("Warning. File not deleted")
            return False
