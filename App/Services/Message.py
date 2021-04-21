from tkinter import messagebox


class Message:

    @staticmethod
    def info(message: str, title: str = "") -> None:
        messagebox.showinfo(title, message)

    @staticmethod
    def warning(message: str, title: str = "") -> None:
        messagebox.showwarning(title, message)

    @staticmethod
    def error(message: str, title: str = "") -> None:
        messagebox.showerror(title, message)

    @staticmethod
    def question(question: str, title: str = "") -> bool:
        if messagebox.askquestion(title, question) == 'yes':
            return True
        return False

    @staticmethod
    def okeycancel(question: str, title: str = "") -> bool:
        if messagebox.askokcancel(title, question) == 'yes':
            return True
        return False

    @staticmethod
    def yesno(question: str, title: str = "") -> bool:
        if messagebox.askyesno(title, question) == 'yes':
            return True
        return False
