from tkinter import Toplevel, IntVar, Checkbutton, X
import tkinter.ttk as ttk
from typing import Any
from App.Controllers.SettingsController import SettingsController


class SettingAppModal:
    top_level_dialog = None
    sms_radio_button = None
    email_radio_button = None
    sms_radio_button_status = None
    email_radio_button_status = None
    theme_status = None

    def __init__(self, master: Any):
        """
        called by INIT
        :param master: ApplicationView window
        """
        self.master = master
        self.title = "Settings"

        settings = SettingsController()
        settings.set_view_settings(self)
        self.sms_radio_button_status = settings.get_sms_config()
        self.email_radio_button_status = settings.get_email_config()

        self.create_top_level_dialog()
        self.set_sms_check_button()
        self.set_email_check_button()
        self.set_black_theme_button()

    def close_modal(self) -> None:
        """
        close setting modal
        :return: None
        """
        config = {"sms_status": self.sms_radio_button_status, "email_status": self.email_radio_button_status}
        SettingsController().set_notification_config(config)
        self.top_level_dialog.destroy()

    def create_top_level_dialog(self) -> None:
        """
        create top level dialog
        :return: None
        """
        self.top_level_dialog = Toplevel(self.master, padx=5, pady=5)
        self.top_level_dialog.title(self.title)
        self.top_level_dialog.minsize(210, 150)
        self.top_level_dialog.maxsize(210, 150)
        self.top_level_dialog.transient(self.master)
        self.top_level_dialog.protocol("WM_DELETE_WINDOW", self.close_modal)

    def set_sms_check_button(self):
        """
        sms on/off notification
        :return: None
        """
        self.sms_radio_button_status = IntVar()

        # Switch
        switch = ttk.Checkbutton(self.top_level_dialog, text='SMS Notification', style='Switch',
                                 variable=self.sms_radio_button_status, offvalue=0, onvalue=1)
        switch.pack(fill=X, expand=False, padx=15, pady=(10, 0))
        switch.invoke()

    def set_email_check_button(self) -> None:
        """
        email on/off notifications
        :return: None
        """
        self.email_radio_button_status = IntVar()

        # Switch
        switch = ttk.Checkbutton(self.top_level_dialog, text='EMAIL Notification', style='Switch',
                                 variable=self.email_radio_button_status, offvalue=0, onvalue=1)
        switch.pack(fill=X, expand=False, padx=15, pady=(10, 0))
        switch.invoke()

    def set_black_theme_button(self) -> None:
        """
        :return:
        """
        print("Theme switching NOT IMPLEMENTED")
        self.theme_status = IntVar()

        # Switch
        switch = ttk.Checkbutton(self.top_level_dialog, text='Night Theme', style='Switch',
                                 variable=self.theme_status, offvalue=0, onvalue=1)
        switch.pack(fill=X, expand=False, padx=15, pady=(10, 0))
        switch.invoke()
