from tkinter import messagebox

class Message:

    def info(self, message:str,  title:str="") -> None:
        messagebox.showinfo(title, message)

    def warning(self, message:str,  title:str="") -> None:
        messagebox.showwarning(title, message)

    def error(self, message:str,  title:str="") -> None:
        messagebox.showerror(title, message)

    def question(self, question:str,  title:str="") -> bool:
        if(messagebox.askquestion(title, question) == 'yes'):
            return True
        return False

    def okeycancel(self, question:str,  title:str="") -> bool:
        if(messagebox.askokcancel(title, question) == 'yes'):
            return True
        return False

    def yesno(self, question:str,  title:str="") -> bool:
        if(messagebox.askyesno(title, question) == 'yes'):
            return True
        return False













