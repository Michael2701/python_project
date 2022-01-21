""" File describe Admin File Process view.
    
    This view help to user start insert data and start interference calculation.
"""

import os
import tkinter
from tkinter import Toplevel, ttk, X
from typing import Any

from App.Controllers.Controller import Controller
from App.Controllers.InterferenceController import InterferenceController
from App.Controllers.SettingsController import SettingsController
from App.Models.GeneticFileModel import GeneticFileModel
from App.Services.FileHelper import FileHelper
from App.Services.Message import Message


class FileProcessModal:
    top_level_dialog = None
    main_frame = None

    PAD_X = 10
    PAD_Y = 10

    step_label = None
    step = None
    step_value = None

    min_distance_label = None
    min_distance = None
    min_distance_value = tkinter.IntVar

    max_distance_label = None
    max_distance = tkinter.IntVar
    max_distance_value = None

    submit_button = None
    cancel_button = None

    separator = None

    file = None
    data = None
    is_excel = None

    def __init__(self, master: Any, genetic_file_ctrl: Controller) -> None:
        """
        Init function
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
        self.set_frame()

        self.set_step_field()
        self.set_separator_line()

        self.set_min_distance_field()
        self.set_separator_line()

        self.set_max_distance_field()
        self.set_separator_line()

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
        self.top_level_dialog = Toplevel(self.master)
        self.top_level_dialog.title(self.title)
        self.top_level_dialog.minsize(300, 100)
        self.top_level_dialog.transient(self.master)
        self.top_level_dialog.protocol("WM_DELETE_WINDOW", self.close_modal)

    def set_frame(self) -> None:
        """
        create frame in view. All content will be show in the frame.
        :return: None
        """
        self.main_frame = ttk.LabelFrame(self.top_level_dialog, text='')
        self.main_frame.pack(fill=X, expand=False)

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

    def set_step_field(self) -> None:
        """
        create email field and label
        :return: None
        """
        self.step_value = tkinter.IntVar()
        self.step_label = ttk.Label(self.main_frame, text="Step")
        self.step_label.pack(fill=X, expand=False, padx=self.PAD_X)

        self.step = ttk.LabeledScale(self.main_frame, from_=1, to=40, variable=self.step_value)
        self.step.pack(fill=X, expand=False, padx=self.PAD_X)

    def set_min_distance_field(self) -> None:
        """
        create password field and label
        :return: None
        """
        self.min_distance_value = tkinter.IntVar()
        self.min_distance_label = ttk.Label(self.main_frame, text="Minimal distance")
        self.min_distance_label.pack(fill=X, expand=False, padx=self.PAD_X)

        self.min_distance = ttk.LabeledScale(self.main_frame, from_=1, to=25, variable=self.min_distance_value)
        self.min_distance.pack(fill=X, expand=False, padx=self.PAD_X)

    def set_max_distance_field(self) -> None:
        """
        create password field and label
        :return: None
        """
        self.max_distance_value = tkinter.IntVar()
        self.max_distance_label = ttk.Label(self.main_frame, text="Maximum distance")
        self.max_distance_label.pack(fill=X, expand=False, padx=self.PAD_X)

        self.max_distance = ttk.LabeledScale(self.main_frame, from_=1, to=25, variable=self.max_distance_value)
        self.max_distance.pack(fill=X, expand=False, padx=self.PAD_X)

    def set_submit_button(self) -> None:
        """
        create submit button
        :return: None
        """
        self.submit_button = ttk.Button(self.main_frame, text='Submit', command=self.on_submit)
        self.submit_button.pack(fill=X, expand=False, padx=self.PAD_X)

    def set_cancel_button(self) -> None:
        """
        crete cancel button
        :return: None
        """
        self.cancel_button = ttk.Button(self.main_frame, text='Cancel', command=self.close_modal)
        self.cancel_button.pack(fill=X, expand=False, padx=self.PAD_X, pady=self.PAD_Y)

    def set_separator_line(self) -> None:
        """
        create separator line on view
        :return: None
        """
        self.separator = ttk.Separator(self.main_frame)
        self.separator.pack(fill=X, expand=False, padx=self.PAD_X, pady=self.PAD_Y)

    def get_form_data(self) -> dict:
        """
        take form data and put it in data dictionary
        :return: dict data
        """
        self.data = {
            'id': self.file.id,
            'step': self.step_value.get(),
            'max_distance': self.max_distance_value.get(),
            'min_distance': self.min_distance_value.get()
        }
        return self.data
