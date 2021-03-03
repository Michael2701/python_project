from tkinter import Entry, Toplevel, Button, Label
from App.Models.UserModel import UserModel

class LoginModal():

    def __init__(self, master, controller):
        self.uctrl = controller
        self.umodel = UserModel()
        self.master = master

        self.title = "Login"
        self.logged_user = None


    def show_toplevel_dialog(self, user=None):
        self.create_modal()

    def create_modal(self):
        self.create_toplevel_dialog()

        self.set_email_field()
        self.set_password_field()

        self.set_submit_button()
        self.set_cancel_button()

    def close_modal(self):
        self.toplevel_dialog.destroy()

    def create_toplevel_dialog(self):
        self.toplevel_dialog = Toplevel(self.master, padx=5, pady=5)
        self.toplevel_dialog.title(self.title)
        self.toplevel_dialog.minsize(300, 100)
        self.toplevel_dialog.transient(self.master)
        self.toplevel_dialog.protocol("WM_DELETE_WINDOW", self.close_modal)

    def on_submit_login(self):
        self.get_form_data()
        print(self.data['email'], self.data['password'])
        user = self.umodel.get_user_by_email(self.data['email'])
        if user is not None:
            self.logged_user = user
            if user[4] == self.data['password']:
                self.uctrl.set_logged_user(user)


    def set_submit_button(self):
        self.submit_button = Button(self.toplevel_dialog, text='Submit', command=self.on_submit_login)
        self.submit_button.grid(row=6, column=0)

    def set_cancel_button(self):
        self.cancel_button = Button(self.toplevel_dialog, text='Cancel', command=self.close_modal)
        self.cancel_button.grid(row=6, column=1)

    def set_email_field(self):
        self.email_label = Label(self.toplevel_dialog, text="Email")
        self.email_label.grid(row=0, column=0)
        self.email_entry = Entry(self.toplevel_dialog)
        self.email_entry.grid(row=1, column=0)

    def set_password_field(self):
        self.password_label = Label(self.toplevel_dialog, text="Password")
        self.password_label.grid(row=2, column=0)
        self.password_entry = Entry(self.toplevel_dialog)
        self.password_entry.grid(row=3, column=0)

    def get_logged_user(self):
        return self.logged_user

    def get_form_data(self):
        data =  {
            'email': self.email_entry.get(),
            'password': self.password_entry.get()
        }

        self.data = data




