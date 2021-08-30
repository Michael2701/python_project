from tkinter import Toplevel, IntVar, Checkbutton
from typing import Any
from App.Controllers.SettingsController import SettingsController


class SettingAppModal:
    top_level_dialog = None
    sms_radio_button = None
    email_radio_button = None
    sms_radio_button_status = None
    email_radio_button_status = None

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

        self.sms_radio_button_status = SettingsController()

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
        self.top_level_dialog.minsize(300, 150)
        self.top_level_dialog.transient(self.master)
        self.top_level_dialog.protocol("WM_DELETE_WINDOW", self.close_modal)

    def set_sms_check_button(self):
        """
        sms on/off notification
        :return: None
        """
        self.sms_radio_button_status = IntVar()
        self.sms_radio_button = Checkbutton(self.top_level_dialog, text="SMS Notification",
                                            variable=self.sms_radio_button_status,
                                            onvalue=1,
                                            offvalue=0,
                                            height=2,
                                            width=15)
        self.sms_radio_button.pack()

    def set_email_check_button(self) -> None:
        """
        email on/off notifications
        :return: None
        """
        self.email_radio_button_status = IntVar()
        self.email_radio_button = Checkbutton(self.top_level_dialog, text="Email Notification",
                                              variable=self.email_radio_button_status,
                                              onvalue=1,
                                              offvalue=0,
                                              height=2,
                                              width=15)
        self.email_radio_button.pack()
