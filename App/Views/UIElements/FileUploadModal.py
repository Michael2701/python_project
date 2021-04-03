import os
from datetime import datetime
from tkinter import Entry, Toplevel, Button, Label
from App.Services.Message import Message
from tkinter import filedialog
from App.Services.FileUploader import FileUploader

class FileUploadModal():

    def __init__(self,window, master):
        self.msg = Message()
        self.window = window
        self.master = master

        self.title = "File upload"
        self.file_path = None
        self.file_name = None
        self.file_description = None
        self.data = []

        self.create_modal()

    def create_modal(self):
        self.create_toplevel_dialog()

        self.set_file_name_field()
        self.set_file_description_field()

        self.set_file_dialog_button()
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

    def on_submit(self):
        if( self.get_form_data() ):
            self.window.create_file(self.data)
            self.close_modal()
        else:
            self.msg.warning("Warning. All fields are required!")

    def open_file_dialog(self):
        self.file_path = filedialog.askopenfilename()

    def set_file_dialog_button(self):
        self.file_dialog_button = Button(self.toplevel_dialog, text='Choose file', command=self.open_file_dialog)
        self.file_dialog_button.grid(row=1, column=1)


    def set_submit_button(self):
        self.submit_button = Button(self.toplevel_dialog, text='Submit', command=self.on_submit)
        self.submit_button.grid(row=6, column=0)

    def set_cancel_button(self):
        self.cancel_button = Button(self.toplevel_dialog, text='Cancel', command=self.close_modal)
        self.cancel_button.grid(row=6, column=1)
    
    def set_file_name_field(self):
        self.file_name_label = Label(self.toplevel_dialog, text="File name")
        self.file_name_label.grid(row=0, column=0)
        self.file_name_entry = Entry(self.toplevel_dialog)
        self.file_name_entry.grid(row=1, column=0)

    def set_file_description_field(self):
        self.file_description_label = Label(self.toplevel_dialog, text="Description")
        self.file_description_label.grid(row=2, column=0)
        self.file_description_entry = Entry(self.toplevel_dialog)
        self.file_description_entry.grid(row=3, column=0)

    def get_form_data(self):

        if( self.check_file_name() and 
            self.check_file_description() and 
            self.check_file_path() and
            self.check_user_id()
        ):

            self.data =  {
                'user_id': str(self.master.logged_user.id),
                'file_name': self.file_name_entry.get(),
                'file_description': self.file_description_entry.get(),
                'file_created_at': datetime.now().strftime("%d/%m/%Y"),
                'file_path': self.file_path
            }
            return True

        return False


    def check_file_name(self):
        try:
            if(len(self.file_name_entry.get()) == 0):
                return False
            
            return True

        except Exception as e:
            print(str(e))
            return False


    def check_file_description(self):
        try:
            if(len(self.file_description_entry.get()) == 0):
                return False
            
            return True

        except Exception as e:
            print(str(e))
            return False


    def check_file_path(self):
        try:
            if(os.path.exists(self.file_path)):
                return True        
            return False
        except Exception as e:
            return False


    def check_user_id(self):
        try:
            if(self.master.logged_user.id != None):
                return True
            return False

        except Exception as e:
            print(str(e))
            return False

         




