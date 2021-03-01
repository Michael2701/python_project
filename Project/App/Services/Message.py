from tkinter import messagebox

class Message:
    def __init__(self):
        pass

    def info(self, message,  title=""):
        messagebox.showinfo(title, message)

    def warning(self, message,  title=""):
        messagebox.showwarning(title, message)

    def error(self, message,  title=""):
        messagebox.showwarning(title, message)

    def question(self, question,  title=""):
        if(messagebox.askquestion(title, question) == 1):
            return True
        return False

    def okeycancel(self, question,  title=""):
        if(messagebox.askokcancel(title, question) == 1):
            return True
        return False

    def yesno(self, question,  title=""):
        if(messagebox.askyesno(title, question) == 1):
            return True
        return False













