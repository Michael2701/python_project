""" File describe Update file view.
    
    This view contain elements for changing genetic file in data base.
"""

from tkinter import Entry, Toplevel, Button, Label, Text, X, ttk
import tkinter as tk
from tkinter.scrolledtext import ScrolledText
from typing import Any

from App.Controllers.SettingsController import SettingsController
from App.Models.GeneticFileModel import GeneticFileModel
from App.Services.Message import Message


class UpdateFileMetaModal:
    file = None
    top_level_dialog = None
    main_frame = None

    submit_button = None
    cancel_button = None
    file_name_label = None
    file_name_entry = None
    file_created_at_label = None
    file_created_at_entry = None
    file_description_label = None
    file_description_entry = None

    PAD_X = 10
    PAD_Y = 10

    def __init__(self, master: Any, ctrl: Any) -> None:
        """
        Init function
        :param master: ApplicationView window
        :param ctrl: Controller
        """
        SettingsController().set_view_settings(self)
        self.msg = Message()

        self.title = "Update file meta"
        self.ctrl = ctrl
        self.master = master
        self.data = []

    def show_top_level_dialog(self, file: GeneticFileModel) -> None:
        """
        show view
        :file: model of genetic file
        :return: None
        """
        self.file = file
        self.create_modal()
        self.set_fields_values()

    def create_modal(self) -> None:
        """
        create modal by calling relevant methods
        :return: None
        """
        self.create_top_level_dialog()
        self.set_frame()

        self.set_file_name_field()
        self.set_file_description_field()
        self.set_file_created_at_field()

        self.set_submit_button()
        self.set_cancel_button()

    def close_modal(self) -> None:
        """
        close modal
        :return: None
        """
        self.top_level_dialog.destroy()

    def update(self) -> None:
        """
        update file in database according user input
        :return: None
        """
        if self.get_form_data():
            self.close_modal()
            self.ctrl.update_file(self.file, self.data)
        else:
            self.msg.warning("Warning. All fields are required")

    def create_top_level_dialog(self) -> None:
        """
        create view
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
        self.main_frame = ttk.LabelFrame(self.top_level_dialog)
        self.main_frame.pack(fill=X, expand=False)

    def set_file_name_field(self) -> None:
        """
        create file name field in view
        :return: None
        """
        self.file_name_label = ttk.Label(self.main_frame, text='File Name')
        self.file_name_label.pack(fill=X, expand=False, padx=self.PAD_X)

        self.file_name_entry = ttk.Entry(self.main_frame)
        self.file_name_entry.pack(fill=X, expand=False, padx=self.PAD_X)

    def set_file_description_field(self) -> None:
        """
        create description file field
        :return: None
        """
        self.file_description_label = ttk.Label(self.main_frame, text="File Description")
        self.file_description_label.pack(fill=X, expand=False, padx=self.PAD_X, pady=(self.PAD_Y, 0))

        self.file_description_entry = ScrolledText(self.main_frame, height=5, width=6)
        self.file_description_entry.pack(fill=X, expand=False, padx=self.PAD_X)

    def set_file_created_at_field(self) -> None:
        """
        create 'created at' filed in view
        :return: None
        """
        self.file_created_at_label = ttk.Label(self.main_frame, text="Created at")
        self.file_created_at_label.pack(fill=X, expand=False, padx=self.PAD_X, pady=(self.PAD_Y, 0))

        self.file_created_at_entry = ttk.Entry(self.main_frame, state='readonly')
        self.file_created_at_entry.pack(fill=X, expand=False, padx=self.PAD_X)

    def set_submit_button(self) -> None:
        """
        create submit button that saved data
        :return: None
        """
        self.submit_button = ttk.Button(self.main_frame, text='Submit', command=self.update)
        self.submit_button.pack(fill=X, expand=False, padx=self.PAD_X, pady=(self.PAD_Y, 0))

    def set_cancel_button(self) -> None:
        """
        close view without any changes
        :return: None
        """
        self.cancel_button = ttk.Button(self.main_frame, text='Cancel', command=self.close_modal)
        self.cancel_button.pack(fill=X, expand=False, padx=self.PAD_X, pady=self.PAD_Y)

    def set_fields_values(self) -> None:
        """
        fill fields if file exists in data base
        :return: None
        """
        if self.file is not None:
            self.set_file_name()
            self.set_file_description()
            self.set_file_created_at()

    def set_file_name(self) -> None:
        """
        fill file name field if file name exists
        :return: None
        """
        if self.file.file_name is not None:
            self.file_name_entry.delete(0, tk.END)
            self.file_name_entry.insert(0, self.file.file_name)

    def set_file_description(self) -> None:
        """
        fill file description if file description exists
        :return: None
        """
        if self.file.file_description is not None:
            self.file_description_entry.delete('1.0', tk.END)
            self.file_description_entry.insert('1.0', self.file.file_description)

    def set_file_created_at(self) -> None:
        """
        fill file creation date if it exists
        :return: None
        """
        if self.file.file_created_at is not None:
            self.file_created_at_entry.configure(state='normal')
            self.file_created_at_entry.delete(0, tk.END)
            self.file_created_at_entry.insert(0, self.file.file_created_at)
            self.file_created_at_entry.configure(state='readonly')

    def get_form_data(self) -> bool:
        """
        save data from fields to variable
        :return: True if data was correct and saved to variable otherwise False
        """
        if self.check_fields():
            data = {
                'id': self.file.id,
                'user_id': self.file.user_id,
                'file_name': self.file_name_entry.get(),
                'file_description': self.file_description_entry.get("1.0", tk.END).strip(),
                'file_created_at': self.file.file_created_at
            }

            self.data = data
            return True
        else:
            return False

    def check_fields(self) -> bool:
        """
        check input fields filled correct
        :return: True if fields found filled correct otherwise False
        """
        return self.check_file_description() and self.check_file_name()

    def check_file_name(self) -> bool:
        """
        check that name field is not empty
        :return: True if file name correct (not empty) otherwise False
        """
        try:
            if len(self.file_name_entry.get()) == 0:
                return False

            return True

        except Exception as e:
            print(str(e))
            return False

    def check_file_description(self) -> bool:
        """
        check if file description correct (not empty)
        :return: True if description correct otherwise False 
        """
        try:
            if len(self.file_description_entry.get("1.0", tk.END).strip()) == 0:
                return False

            return True

        except Exception as e:
            print(str(e))
            return False
