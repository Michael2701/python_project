from textwrap import wrap
from tkinter import *
from tkinter.ttk import Frame
from typing import Any, List

from App.Controllers.SettingsController import SettingsController
from App.Models.GeneticFileModel import GeneticFileModel


class GeneticFilesView(Canvas):
    __ctrl: SettingsController
    __master: Tk
    __frame: Frame
    __files: List[GeneticFileModel]

    def __init__(self, ctrl: SettingsController, master: Tk, files: GeneticFileModel):
        """
        :param ctrl: view controller
        :param master: parent view
        :param files: GeneticFileModel object list
        """
        Canvas.__init__(self, master, width=500, height=1000)

        scroll = Scrollbar(self, command=self.yview)
        self.config(yscrollcommand=scroll.set, scrollregion=(0, 0, 500, 1000))
        self.pack(side=LEFT, fill=BOTH, expand=True)
        scroll.pack(side=RIGHT, fill=Y)

        self.frame = Frame(self, width=500, height=1000)
        self.create_window((400, 260), window=self.frame)

        SettingsController().set_view_settings(self)
        self.ctrl = ctrl
        self.master = master
        self.files = files
        self.init_window()

    def init_window(self) -> None:
        """
        init files view window
        :return: None
        """
        self.create_table()
        self.create_table_titles()
        self.pack(fill='both')

    def create_table_titles(self) -> None:
        """
        create files table titles
        :return: None
        """
        label = Label(self.frame, text="#", bg=self.bg, fg=self.fg, font=self.title_font)
        label.grid(row=0, column=0, padx=3, pady=3)

        label = Label(self.frame, text="Name", bg=self.bg, fg=self.fg, font=self.title_font)
        label.grid(row=0, column=1, padx=3, pady=3)

        label = Label(self.frame, text="Description", bg=self.bg, fg=self.fg, font=self.title_font)
        label.grid(row=0, column=2, padx=3, pady=3)

        label = Label(self.frame, text="Created at", bg=self.bg, fg=self.fg, font=self.title_font)
        label.grid(row=0, column=3, padx=3, pady=3)

        label = Label(self.frame, text="", bg=self.bg, fg=self.fg, font=self.title_font)
        label.grid(row=0, column=4, padx=3, pady=3)

        label = Label(self.frame, text="", bg=self.bg, fg=self.fg, font=self.title_font)
        label.grid(row=0, column=5, padx=3, pady=3)

    @staticmethod
    def break_string(s) -> str:
        """
        break given string with '\n'
        :param s: string to break
        :return: string
        """
        return '\n'.join(wrap(s, 35))

    def create_table(self) -> None:
        """
        create table of files from given list
        :return: None
        """
        row = 1

        for file in self.files:
            label = Label(self.frame, text=file.id, bg=self.bg, fg=self.fg, font=self.font, width=5)
            label.grid(row=row, column=0, padx=3, pady=3)

            label = Label(self.frame, text=file.file_name, bg=self.bg, fg=self.fg, font=self.font, width=20)
            label.grid(row=row, column=1, padx=3, pady=3)

            label = Label(self.frame, text=self.break_string(file.file_description), bg=self.bg, fg=self.fg, font=self.font, width=30)
            label.grid(row=row, column=2, padx=3, pady=3)

            label = Label(self.frame, text=file.file_created_at, bg=self.bg, fg=self.fg, font=self.font, width=11)
            label.grid(row=row, column=3, padx=3, pady=3)

            button = Button(self.frame, text="Interference", font=self.font, fg=self.fg, command=lambda f=file: self.ctrl.open_file_process_modal(f, False))
            button.grid(row=row, column=4, padx=3, pady=3)

            button = Button(self.frame, text="Excel", font=self.font, fg=self.fg, command=lambda f=file: self.ctrl.open_file_process_modal(f, True), )
            button.grid(row=row, column=5, padx=3, pady=3)

            button = Button(self.frame, text="Update", font=self.font, fg=self.fg, command=lambda f=file: self.ctrl.show_update_file_modal(f))
            button.grid(row=row, column=6, padx=3, pady=3)

            button = Button(self.frame, text="Delete", font=self.font, fg=self.fg, command=lambda f=file: self.ctrl.show_delete_modal(f))
            button.grid(row=row, column=7, padx=3, pady=3)

            row += 1

    @property
    def files(self) -> List[GeneticFileModel]:
        return self.__files

    @files.setter
    def files(self, files: List[GeneticFileModel]) -> None:
        self.__files = files

    @property
    def master(self) -> Tk:
        return self.__master

    @master.setter
    def master(self, master: Tk) -> None:
        self.__master = master

    @property
    def ctrl(self) -> SettingsController:
        return self.__ctrl

    @ctrl.setter
    def ctrl(self, ctrl: SettingsController) -> None:
        self.__ctrl = ctrl

    @property
    def frame(self) -> Frame:
        return self.__frame

    @frame.setter
    def frame(self, frame: Frame) -> None:
        self.__frame = frame

