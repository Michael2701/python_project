from tkinter import Entry, Toplevel, Button, Label
import tkinter as tk

class UpdateUserPopup(tk.Tk):

    def __init__(self, master, user):
        tk.Tk.__init__(self)
        self.master = master
        self.user = user
        self.create_modal()

    def create_modal(self):

        self.toplevel_dialog = Toplevel(self.master, padx=5, pady=5)
        self.toplevel_dialog.minsize(300, 100)
        self.toplevel_dialog.transient() # self || self.master ?

        self.toplevel_dialog.protocol("WM_DELETE_WINDOW", self.close_modal)

        self.first_name_label = Label(self.toplevel_dialog, text='First Name')
        self.first_name_label.grid(row=0, column=0)
        self.first_name_entry = Entry(self.toplevel_dialog)
        self.first_name_entry.grid(row=1, column=0)

        self.last_name_label = Label(self.toplevel_dialog, text="Last Name")
        self.last_name_label.grid(row=0, column=1)
        self.last_name_entry = Entry(self.toplevel_dialog)
        self.last_name_entry.grid(row=1, column=1)

        self.email_label = Label(self.toplevel_dialog, text="Email")
        self.email_label.grid(row=2, column=0)
        self.email_entry = Entry(self.toplevel_dialog)
        self.email_entry.grid(row=3, column=0)

        self.user_role_label = Label(self.toplevel_dialog, text="User Role")
        self.user_role_label.grid(row=2, column=1)
        self.user_role_entry = Entry(self.toplevel_dialog)
        self.user_role_entry.grid(row=3, column=1)

        self.toplevel_dialog_yes_button = Button(self.toplevel_dialog, text='Submit')
        self.toplevel_dialog_yes_button.grid(row=4, column=0)

        self.toplevel_dialog_no_button = Button(self.toplevel_dialog, text='Cancel', command=self.close_modal)
        self.toplevel_dialog_no_button.grid(row=4, column=1)

    def close_modal(self):
        self.toplevel_dialog.destroy()

    def update(self):
        pass