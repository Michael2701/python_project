from tkinter import Entry, OptionMenu, StringVar, Toplevel, Button, Label
import tkinter as tk
from tkinter.ttk import Combobox


class UpdateFileMetaModal():

    def __init__(self, master, ctrl):
        self.title = "Update file meta"
        self.ctrl = ctrl
        self.master = master
        self.data = []

    def show_toplevel_dialog(self, file):
        self.file = file
        self.create_modal()
        self.set_fields_values()

    def create_modal(self):
        self.create_toplevel_dialog()

        self.set_file_name_field()
        self.set_file_description_field()
        self.set_file_created_at_field()

        self.set_submit_button()
        self.set_cancel_button()

    def close_modal(self):
        self.toplevel_dialog.destroy()

    def update(self):
        self.get_form_data()
        self.close_modal()
        self.ctrl.update_file(self.file, self.data)


    def create_toplevel_dialog(self):
        self.toplevel_dialog = Toplevel(self.master, padx=5, pady=5)
        self.toplevel_dialog.title(self.title)
        self.toplevel_dialog.minsize(300, 100)
        self.toplevel_dialog.transient(self.master)
        self.toplevel_dialog.protocol("WM_DELETE_WINDOW", self.close_modal)


    def set_submit_button(self):
        self.submit_button = Button(self.toplevel_dialog, text='Submit', command=self.update)
        self.submit_button.grid(row=6, column=0)


    def set_cancel_button(self):
        self.cancel_button = Button(self.toplevel_dialog, text='Cancel', command=self.close_modal)
        self.cancel_button.grid(row=6, column=1)


    def set_file_name_field(self):
        self.file_name_label = Label(self.toplevel_dialog, text='File Name')
        self.file_name_label.grid(row=0, column=0)
        self.file_name_entry = Entry(self.toplevel_dialog)
        self.file_name_entry.grid(row=1, column=0)

    def set_file_description_field(self):
        self.file_description_label = Label(self.toplevel_dialog, text="File Description")
        self.file_description_label.grid(row=0, column=1)
        self.file_description_entry = Entry(self.toplevel_dialog)
        self.file_description_entry.grid(row=1, column=1)

    def set_file_created_at_field(self):
        self.file_created_at_label = Label(self.toplevel_dialog, text="Created at")
        self.file_created_at_label.grid(row=2, column=0)
        self.file_created_at_entry = Entry(self.toplevel_dialog)
        self.file_created_at_entry.grid(row=3, column=0)


    def set_fields_values(self):
        if(self.file is not None):
            self.set_file_name()
            self.set_file_description()
            self.set_file_created_at()

    def set_file_name(self):
        if(self.file.file_name is not None):
            self.file_name_entry.delete(0, tk.END)
            self.file_name_entry.insert(0, self.file.file_name)

    def set_file_description(self):
        if(self.file.file_description is not None):
            self.file_description_entry.delete(0, tk.END)
            self.file_description_entry.insert(0, self.file.file_description)

    def set_file_created_at (self):
        if(self.file.file_created_at  is not None):
            self.file_created_at_entry.delete(0, tk.END)
            self.file_created_at_entry.insert(0, self.file.file_created_at )

    def get_form_data(self):
        data =  {
            'id' : self.file.id,
            'user_id' : self.file.user_id,
            'file_name': self.file_name_entry.get(),
            'file_description': self.file_description_entry.get(),
            'file_created_at': self.file_created_at_entry.get()
        }

        self.data = data




