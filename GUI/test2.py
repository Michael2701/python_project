from tkinter import *

class Window (Frame):
    def __init__(self, master = None):
        Frame.__init__(self,master)

        self.master = master
        self.init_window()

    def init_window(self):
        self.master.title("Please send help thanks.")

        self.pack(fill=BOTH, expand=1)

        menu = Menu(self.master)
        self.master.config(menu=menu)

        file = Menu(menu, tearoff=0)
        file.add_command(label='Open')
        file.add_command(label='Exit', command=self.client_exit)
        menu.add_cascade(label='File', menu=file)

        edit = Menu(menu, tearoff=0)
        edit.add_command(label='Show Text', command=self.showTxt)
        menu.add_cascade(label='Edit', menu=edit)

        help = Menu(menu, tearoff=0)
        help.add_command(label='Help Index')
        help.add_command(label='About Us')
        menu.add_cascade(label='Help', menu=help)

    def showTxt(self):
        text = Label(self, text='Good morning sir!')
        text.pack()

    def client_exit(self):
        exit()

# root = Tk()
# root.geometry("400x300")
# app = Window(root)
# root.mainloop()