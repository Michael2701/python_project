import os
from datetime import datetime
import tkinter as tk
from tkinter import Entry, Toplevel, Button, Label, Text
from typing import Any

from App.Services.Message import Message
from tkinter import filedialog
from App.Services.FileUploader import FileUploader
from App.Controllers.SettingsController import SettingsController


class FileUploadModal:
    submit_button = None
    cancel_button = None
    file_name_label = None
    file_name_entry = None
    top_level_dialog = None
    file_dialog_button = None
    file_description_label = None
    file_description_entry = None

    def __init__(self, ctrl: Any, master: Any):
        """
        :param ctrl: modal controller
        :param master: parent view
        """
        self.msg = Message()
        self.ctrl = ctrl
        self.master = master

        SettingsController().set_view_settings(self)

        self.title = "File upload"
        self.file_path = None
        self.file_name = None
        self.file_description = None
        self.data = []

        self.create_modal()

    def create_modal(self) -> None:
        """
        init file upload modal
        :return: None
        """
        self.create_toplevel_dialog()

        self.set_file_name_field()
        self.set_file_description_field()

        self.set_file_dialog_button()
        self.set_submit_button()
        self.set_cancel_button()

    def close_modal(self) -> None:
        """
        close modal
        :return: None
        """
        self.top_level_dialog.destroy()

    def create_toplevel_dialog(self) -> None:
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
        create file via file controller
        :return: None
        """
        if self.get_form_data():
            self.ctrl.create_file(self.data)
            self.close_modal()
        else:
            self.msg.warning("Warning. All fields are required!")

    def open_file_dialog(self) -> None:
        """
        open choose file dialog
        :return: None
        """
        self.file_path = filedialog.askopenfilename()

        self.file_name_entry.delete(0, tk.END)
        self.file_name_entry.configure(state='normal')
        self.file_name_entry.insert(0, self.file_path.split("/")[-1])
        self.file_name_entry.configure(state='readonly')

    def set_file_dialog_button(self) -> None:
        """
        create file dialog button
        :return: None
        """
        self.file_dialog_button = Button(self.top_level_dialog, text='Choose file', font=self.font, fg=self.fg, command=self.open_file_dialog)
        self.file_dialog_button.grid(row=1, column=1)

    def set_submit_button(self) -> None:
        """
        create submit button
        :return: None
        """
        self.submit_button = Button(self.top_level_dialog, text='Submit', font=self.font, fg=self.fg, command=self.on_submit)
        self.submit_button.grid(row=6, column=0)

    def set_cancel_button(self) -> None:
        """
        create cancel button
        :return: None
        """
        self.cancel_button = Button(self.top_level_dialog, text='Cancel', font=self.font, fg=self.fg, command=self.close_modal)
        self.cancel_button.grid(row=6, column=1)
    
    def set_file_name_field(self) -> None:
        """
        create file name field and label
        :return: None
        """
        self.file_name_label = Label(self.top_level_dialog, bg=self.bg_modal, fg=self.fg, font=self.font, text="File name")
        self.file_name_label.grid(row=0, column=0)
        self.file_name_entry = Entry(self.top_level_dialog, state='readonly')
        self.file_name_entry.grid(row=1, column=0)

    def set_file_description_field(self) -> None:
        """
        create file description filed and label
        :return: None
        """
        self.file_description_label = Label(self.top_level_dialog, bg=self.bg_modal, fg=self.fg, font=self.font, text="Description")
        self.file_description_label.grid(row=2, column=0)
        self.file_description_entry = Text(self.top_level_dialog, height=3, width=6)
        self.file_description_entry.grid(row=3, column=0, columnspan=2, sticky=tk.W+tk.E)

    def get_form_data(self) -> bool:
        """
        get form data end put it on the object
        :return:True if form data is valid and false otherwise
        """
        if self.check_file_name() and self.check_file_description() and self.check_file_path() and self.check_user_id():

            self.data = {
                'user_id': str(self.master.logged_user.id),
                'file_name': self.file_name_entry.get(),
                'file_description': self.file_description_entry.get("1.0", tk.END).strip(),
                'file_created_at': datetime.now().strftime("%d/%m/%Y"),
                'file_path': self.file_path
            }
            return True

        return False

    def check_file_name(self) -> bool:
        """
        check if value of file name is valid
        :return: True if valid and False otherwise
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
        check if value of file description is vald
        :return: True if valid and False otherwise
        """
        try:
            if len(self.file_description_entry.get("1.0", tk.END).strip()) == 0:
                return False
            
            return True

        except Exception as e:
            print(str(e))
            return False

    def check_file_path(self) -> bool:
        """
        check if file path exists
        :return: True if exists and False otherwise
        """
        try:
            if os.path.exists(self.file_path) and os.path.isfile(self.file_path):
                return True        
            return False

        except FileExistsError as e:
            print(str(e))
            return False

    def check_user_id(self) -> bool:
        """
        check if logged user id exists
        :return: True if exists and False otherwise
        """
        try:
            if self.master.logged_user.id is not None:
                return True
            return False

        except Exception as e:
            print(str(e))
            return False

         




