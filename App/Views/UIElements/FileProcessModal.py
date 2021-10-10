import os
from typing import Any
from tkinter import Toplevel, Button, Label, Scale, HORIZONTAL

from App.Controllers.InterferenceController import InterferenceController
from App.Controllers.SettingsController import SettingsController
# from App.Controllers.GeneticFileController import GeneticFileController

from App.Models.GeneticFileModel import GeneticFileModel
from App.Services.FileHelper import FileHelper
from App.Services.Message import Message
from App.Controllers.Controller import Controller
from App.Controllers.SettingsController import SettingsController


class FileProcessModal:
    top_level_dialog = None
    submit_button = None
    cancel_button = None
    min_distance_label = None
    min_distance_entry = None
    max_distance_entry = None
    max_distance_label = None
    step_label = None
    step_entry = None
    file = None
    data = None
    is_excel = None

    def __init__(self, master: Any, genetic_file_ctrl: Controller) -> None:
        """
        :param master: ApplicationView window
        :param genetic_file_ctrl: GeneticFileController
        """
        self.genetic_file_ctrl = genetic_file_ctrl
        self.master = master

        SettingsController().set_view_settings(self)

        self.title = "Create Interference"
        self.logged_user = None
        self.is_excel = True

        self.create_modal()

    def show_top_level_dialog(self, file: GeneticFileModel, is_excel: bool) -> None:
        """
        show login modal
        :return: None
        """
        self.is_excel = is_excel
        self.file = file
        self.create_modal()

    def create_modal(self) -> None:
        """
        init login modal
        :return: None
        """
        self.create_top_level_dialog()

        self.set_step_field()
        self.set_min_distance_field()
        self.set_max_distance_field()

        self.set_submit_button()
        self.set_cancel_button()

    def close_modal(self) -> None:
        """
        close login modal
        :return: None
        """
        self.top_level_dialog.destroy()

    def create_top_level_dialog(self) -> None:
        """
        create top level dialog
        :return: None
        """
        self.top_level_dialog = Toplevel(self.master, padx=5, pady=5)
        self.top_level_dialog.title(self.title)
        self.top_level_dialog.minsize(300, 100)
        self.top_level_dialog.transient(self.master)
        self.top_level_dialog.protocol("WM_DELETE_WINDOW", self.close_modal)

    def on_submit(self) -> None:
        """
        :return: None
        """
        file_triplet_name = 'App/triplet_of_genes.csv'
        self.get_form_data()
        if self.check_form_data():
            self.close_modal()
            self.genetic_file_ctrl.process_file_genes(self.data)
            if self.is_excel:
                self.genetic_file_ctrl.create_markers_statistic_excel()
            else:

                if os.path.exists(file_triplet_name):
                    os.remove(file_triplet_name)
                FileHelper.write_list_to_csv(file_triplet_name, self.genetic_file_ctrl.create_list_of_markers())
                InterferenceController().create_interference(self.file, self.data)

    def check_form_data(self):
        if self.data["min_distance"] >= self.data["max_distance"]:
            Message.error("Min distance must be smaller then max")
            return False
        return True

    def set_submit_button(self) -> None:
        """
        create submit button
        :return: None
        """
        self.submit_button = Button(self.top_level_dialog, text='Submit', font=self.font, fg=self.fg,
                                    command=self.on_submit)
        self.submit_button.grid(row=6, column=0)

    def set_cancel_button(self) -> None:
        """
        crete cancel button
        :return: None
        """
        self.cancel_button = Button(self.top_level_dialog, text='Cancel', font=self.font, fg=self.fg,
                                    command=self.close_modal)
        self.cancel_button.grid(row=6, column=1)

    def set_step_field(self) -> None:
        """
        create email field and label
        :return: None
        """
        self.step_label = Label(self.top_level_dialog, bg=self.bg, fg=self.fg, font=self.font, text="Step")
        self.step_label.grid(row=0, column=0)
        self.step_entry = Scale(self.top_level_dialog, from_=1, to=42, length=300, orient=HORIZONTAL)
        self.step_entry.grid(row=0, column=1)

    def set_min_distance_field(self) -> None:
        """
        create password field and label
        :return: None
        """
        self.min_distance_label = Label(self.top_level_dialog, bg=self.bg, fg=self.fg, font=self.font,
                                        text="Min distance")
        self.min_distance_label.grid(row=1, column=0)
        self.min_distance_entry = Scale(self.top_level_dialog, from_=1, to=25, length=300, orient=HORIZONTAL)
        self.min_distance_entry.grid(row=1, column=1)

    def set_max_distance_field(self) -> None:
        """
        create password field and label
        :return: None
        """
        self.max_distance_label = Label(self.top_level_dialog, bg=self.bg, fg=self.fg, font=self.font,
                                        text="Max distance")
        self.max_distance_label.grid(row=2, column=0)
        self.max_distance_entry = Scale(self.top_level_dialog, from_=1, to=25, length=300, orient=HORIZONTAL)
        self.max_distance_entry.grid(row=2, column=1)

    def get_form_data(self) -> dict:
        """
        take form data and put it in self.data dictionary
        :return: dict self.data
        """
        self.data = {
            'id': self.file.id,
            'step': self.step_entry.get(),
            'max_distance': self.max_distance_entry.get(),
            'min_distance': self.min_distance_entry.get()
        }
        return self.data
