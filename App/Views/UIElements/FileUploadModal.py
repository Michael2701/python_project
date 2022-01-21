""" File describe File uploading view.
    
    This view help to user choose and start .
"""

import os
import tkinter as tk
import tkinter.ttk as ttk
from datetime import datetime
from tkinter import Entry, Toplevel, Button, Label, IntVar, X, LEFT
from tkinter import filedialog
from tkinter.scrolledtext import ScrolledText
from typing import Any

from App.Services.Message import Message


class FileUploadModal:
    __submit_button: Button
    __cancel_button: Button
    __file_name_label: Label
    __file_name_entry: Entry
    __top_level_dialog: Toplevel
    __main_frame: ttk.LabelFrame
    __file_dialog_button: Button
    __file_description_label: Label
    __file_description_entry: Entry
    __progress_value: IntVar
    __separator: ttk.Separator

    PAD_X = 10
    PAD_Y = 10

    @property
    def file_description_entry(self) -> Entry:
        return self.__file_description_entry

    @file_description_entry.setter
    def file_description_entry(self, entry: Entry) -> None:
        self.__file_description_entry = entry

    @property
    def file_description_label(self) -> Label:
        return self.__file_description_label

    @file_description_label.setter
    def file_description_label(self, label: Label) -> None:
        self.__file_description_label = label

    @property
    def file_dialog_button(self) -> Button:
        return self.__file_dialog_button

    @file_dialog_button.setter
    def file_dialog_button(self, button: Button) -> None:
        self.__file_dialog_button = button

    @property
    def top_level_dialog(self) -> Toplevel:
        return self.__top_level_dialog

    @top_level_dialog.setter
    def top_level_dialog(self, top_level: Toplevel) -> None:
        self.__top_level_dialog = top_level

    @property
    def main_frame(self) -> ttk.LabelFrame:
        return self.__main_frame

    @main_frame.setter
    def main_frame(self, main_frame: ttk.LabelFrame) -> None:
        self.__main_frame = main_frame

    @property
    def file_name_entry(self) -> Entry:
        return self.__file_name_entry

    @file_name_entry.setter
    def file_name_entry(self, entry: Entry) -> None:
        self.__file_name_entry = entry

    @property
    def file_name_label(self) -> Label:
        return self.__file_name_label

    @file_name_label.setter
    def file_name_label(self, label: Label) -> None:
        self.__file_name_label = label

    @property
    def cancel_button(self) -> Button:
        return self.__cancel_button

    @cancel_button.setter
    def cancel_button(self, button: Button) -> None:
        self.__cancel_button = button

    @property
    def submit_button(self) -> Button:
        return self.__submit_button

    @submit_button.setter
    def submit_button(self, button: Button) -> None:
        self.__submit_button = button

    @property
    def separator(self) -> ttk.Separator:
        return self.__separator

    @separator.setter
    def separator(self, sep: ttk.Separator) -> None:
        self.__separator = sep

    def __init__(self, ctrl: Any, master: Any):
        """
        Init function
        :param ctrl: modal controller
        :param master: parent view
        """
        self.msg = Message()
        self.ctrl = ctrl
        self.master = master

        self.title = "File upload"
        self.__main_frame = None
        self.file_path = None
        self.file_name = None
        self.file_description = None
        self.progress_bar = None
        self.__progress_value = IntVar()
        self.data = []

        self.create_modal()

    def create_modal(self) -> None:
        """
        init file upload modal
        :return: None
        """
        self.create_top_level_dialog()
        self.set_frame()

        self.set_file_name_fields()
        self.set_file_description_field()

        self.set_submit_button()
        self.set_cancel_button()

        # self.set_progress_bar()

    def close_modal(self) -> None:
        """
        close modal
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
        self.main_frame = ttk.LabelFrame(self.top_level_dialog)
        self.main_frame.pack(fill=X, expand=False)

    def set_submit_button(self) -> None:
        """
        create submit button
        :return: None
        """
        self.submit_button = ttk.Button(self.main_frame, text='Submit', command=self.on_submit)
        self.submit_button.pack(fill=X, expand=False, padx=self.PAD_X, pady=(self.PAD_Y, 0))

    def on_submit(self) -> None:
        """
        create file via file controller
        :return: None
        """
        if self.get_form_data():
            self.animate_progress_bar()
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

    def set_cancel_button(self) -> None:
        """
        create cancel button
        :return: None
        """
        self.cancel_button = ttk.Button(self.main_frame, text='Cancel', command=self.close_modal)
        self.cancel_button.pack(fill=X, expand=False, padx=self.PAD_X, pady=self.PAD_Y)

    def set_progress_bar(self) -> None:
        """
        set progress loading bar on view
        :return: None
        """
        self.progress_bar = ttk.Progressbar(self.main_frame, value=0, variable=self.__progress_value, mode='determinate')
        self.progress_bar.pack(fill=X, expand=False, padx=self.PAD_X)

    def increment_progress_bar(self, step: int) -> None:
        """
        increment progress value by step
        :param step: incrementing value
        :return: None
        """
        self.progress_bar.step(step)

    def animate_progress_bar(self, step: int = None):
        """
        start progress bar animation
        :param step: interval defaults to 50 milliseconds (20 steps/second) if omitted.
        :return: None
        """
        self.progress_bar.start(step)

    def set_file_name_fields(self) -> None:
        """
        create file name field, label and button
        :return: None
        """
        self.file_name_label = ttk.Label(self.main_frame, text="File name")
        self.file_name_label.pack(fill=X, expand=False, padx=self.PAD_X)

        frame = tk.Frame(self.main_frame)
        frame.pack(fill=tk.X)

        self.file_name_entry = ttk.Entry(frame, width=30, state='readonly')
        self.file_name_entry.pack(side=LEFT, expand=False, padx=self.PAD_X)

        self.file_dialog_button = ttk.Button(frame, text='Choose file', command=self.open_file_dialog)
        self.file_dialog_button.pack(fill=X, expand=False, padx=(0, self.PAD_X))

    def set_file_description_field(self) -> None:
        """
        create file description filed and label
        :return: None
        """
        self.file_description_label = ttk.Label(self.main_frame, text="Description")
        self.file_description_label.pack(fill=X, expand=False, padx=self.PAD_X, pady=(self.PAD_Y, 0))

        self.file_description_entry = ScrolledText(self.main_frame, height=3, width=6)
        self.file_description_entry.pack(fill=X, expand=False, padx=self.PAD_X)

    def set_separator_line(self) -> None:
        """
        create separator line on view
        :return: None
        """
        self.separator = ttk.Separator(self.main_frame)
        self.separator.pack(fill=X, expand=False, padx=self.PAD_X, pady=(self.PAD_Y, self.PAD_Y))

    def get_form_data(self) -> bool:
        """
        get form data end put it on the object
        :return:True if form data is valid and false otherwise
        """
        if self.check_file_name() and self.check_file_description() and self.check_file_path() and self.check_user_id():
            self.data = {
                'user_id': str(self.ctrl.user["id"]),
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
        check if value of file description is valid
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
            if self.ctrl.user["id"] is not None:
                return True
            return False

        except Exception as e:
            print(str(e))
            return False
