from tkinter import Entry, Toplevel, Button, Label, Text
import tkinter as tk
from typing import Any

from App.Controllers.SettingsController import SettingsController
from App.Models.GeneticFileModel import GeneticFileModel
from App.Services.Message import Message


class UpdateFileMetaModal:
    file = None
    top_level_dialog = None
    submit_button = None
    cancel_button = None
    file_name_label = None
    file_name_entry = None
    file_created_at_label = None
    file_created_at_entry = None
    file_description_label = None
    file_description_entry = None

    def __init__(self, master: Any, ctrl: Any) -> None:
       
        SettingsController().set_view_settings(self)
        self.msg = Message()

        self.title = "Update file meta"
        self.ctrl = ctrl
        self.master = master
        self.data = []

    def show_top_level_dialog(self, file: GeneticFileModel) -> None:
        """

        :type file: object
        """
        self.file = file
        self.create_modal()
        self.set_fields_values()

    def create_modal(self) -> None:
        self.create_top_level_dialog()

        self.set_file_name_field()
        self.set_file_description_field()
        self.set_file_created_at_field()

        self.set_submit_button()
        self.set_cancel_button()

    def close_modal(self) -> None:
        self.top_level_dialog.destroy()

    def update(self) -> None:
        if self.get_form_data():
            self.close_modal()
            self.ctrl.update_file(self.file, self.data)
        else:
            self.msg.warning("Warning. All fields are required")

    def create_top_level_dialog(self) -> None:
        self.top_level_dialog = Toplevel(self.master, padx=5, pady=5)
        self.top_level_dialog.title(self.title)
        self.top_level_dialog.minsize(300, 100)
        self.top_level_dialog.transient(self.master)
        self.top_level_dialog.protocol("WM_DELETE_WINDOW", self.close_modal)

    def set_submit_button(self) -> None:
        self.submit_button = Button(self.top_level_dialog, text='Submit', fg=self.fg, font=self.font, command=self.update)
        self.submit_button.grid(row=6, column=0)

    def set_cancel_button(self) -> None:
        self.cancel_button = Button(self.top_level_dialog, text='Cancel', fg=self.fg, font=self.font, command=self.close_modal)
        self.cancel_button.grid(row=6, column=1)

    def set_file_name_field(self) -> None:
        self.file_name_label = Label(self.top_level_dialog, bg=self.bg_modal, fg=self.fg, font=self.font, text='File Name')
        self.file_name_label.grid(row=0, column=0)
        self.file_name_entry = Entry(self.top_level_dialog)
        self.file_name_entry.grid(row=1, column=0)

    def set_file_created_at_field(self) -> None:
        self.file_created_at_label = Label(self.top_level_dialog, bg=self.bg_modal, fg=self.fg, font=self.font, text="Created at")
        self.file_created_at_label.grid(row=0, column=1)
        self.file_created_at_entry = Entry(self.top_level_dialog, state='readonly')
        self.file_created_at_entry.grid(row=1, column=1)

    def set_file_description_field(self) -> None:
        self.file_description_label = Label(self.top_level_dialog, bg=self.bg_modal, fg=self.fg, font=self.font, text="File Description")
        self.file_description_label.grid(row=2, column=0)
        self.file_description_entry = Text(self.top_level_dialog, height=3, width=6)
        self.file_description_entry.grid(row=3, column=0, columnspan=2, sticky=tk.W+tk.E)

    def set_fields_values(self) -> None:
        if self.file is not None:
            self.set_file_name()
            self.set_file_description()
            self.set_file_created_at()

    def set_file_name(self) -> None:
        if self.file.file_name is not None:
            self.file_name_entry.delete(0, tk.END)
            self.file_name_entry.insert(0, self.file.file_name)

    def set_file_description(self) -> None:
        if self.file.file_description is not None:
            self.file_description_entry.delete('1.0', tk.END)
            self.file_description_entry.insert('1.0', self.file.file_description)

    def set_file_created_at(self) -> None:
        if self.file.file_created_at  is not None:
            self.file_created_at_entry.configure(state='normal')
            self.file_created_at_entry.delete(0, tk.END)
            self.file_created_at_entry.insert(0, self.file.file_created_at )
            self.file_created_at_entry.configure(state='readonly')

    def get_form_data(self) -> bool:
        if self.check_fields():
            data =  {
                'id' : self.file.id,
                'user_id' : self.file.user_id,
                'file_name': self.file_name_entry.get(),
                'file_description': self.file_description_entry.get("1.0",tk.END).strip(),
                'file_created_at': self.file.file_created_at
            }

            self.data = data
            return True
        else:
            return False

    def check_fields(self) -> bool:
        return self.check_file_description() and self.check_file_name()

    def check_file_name(self) -> bool:
        try:
            if len(self.file_name_entry.get()) == 0:
                return False
            
            return True

        except Exception as e:
            print(str(e))
            return False

    def check_file_description(self) -> bool:
        try:
            if len(self.file_description_entry.get("1.0", tk.END).strip()) == 0:
                return False
            
            return True

        except Exception as e:
            print(str(e))
            return False

