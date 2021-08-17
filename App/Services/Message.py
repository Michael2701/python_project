from tkinter import messagebox


class Message:
    """
    wrapper for messagebox
    """

    @staticmethod
    def info(message: str, title: str = "") -> None:
        """
        show info message
        :param message: string message to show
        :param title: string message title
        :return: None
        """
        messagebox.showinfo(title, message)

    @staticmethod
    def warning(message: str, title: str = "") -> None:
        """
        show warning message
        :param message: string message to show
        :param title: string message title
        :return: None
        """
        messagebox.showwarning(title, message)

    @staticmethod
    def error(message: str, title: str = "") -> None:
        """
        show error message
        :param message: string message to show
        :param title: string message title
        :return: None
        """
        messagebox.showerror(title, message)

    @staticmethod
    def question(question: str, title: str = "") -> bool:
        """
        show question
        :param question: string question to ask
        :param title: string question title title
        :return: True if answer is positive and False otherwise
        """
        if messagebox.askquestion(title, question) == 'yes':
            return True
        return False

    @staticmethod
    def yesno(question: str, title: str = "") -> bool:
        """
        show yes or no modal
        :param question: string question to ask
        :param title: string question title
        :return: True if answer is positive and False otherwise
        """
        if messagebox.askyesno(title, question) == 'yes':
            return True
        return False


def okay_cancel(question: str, title: str = "") -> bool:
    """
    show okay and cancel modal
    :param question: string question to ask
    :param title: string question title
    :return: True if answer is positive and False otherwise
    """
    if messagebox.askokcancel(title, question) == 'yes':
        return True
    return False
