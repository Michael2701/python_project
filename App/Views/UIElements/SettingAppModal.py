""" File describe Settings App view.
    
    This view contain elements of settings App.
"""

from tkinter import Toplevel, IntVar, X
import tkinter.ttk as ttk
from typing import Any

from App.Controllers.SettingsController import SettingsController


class SettingAppModal:
    top_level_dialog = None
    main_frame = None
    sms_radio_button = None
    email_radio_button = None
    sms_switch_status = None
    email_switch_status = None
    theme_switch_status = None
    app_theme = None

    PAD_X = 10
    PAD_Y = 10

    night_theme = "App/Azure-ttk-theme/azure dark/azure dark.tcl"
    day_theme = "App/Azure-ttk-theme/azure/azure.tcl"

    def __init__(self, master: Any):
        """
        Init function
        :param master: ApplicationView window
        """
        self.master = master
        self.title = "Settings"

        settings = SettingsController()
        settings.set_view_settings(self)

        self.sms_status = settings.get_sms_notification_status()
        self.email_status = settings.get_email_notification_status()
        self.app_theme = settings.get_theme_path()

        self.create_top_level_dialog()
        self.set_frame()
        self.set_sms_switch()
        self.set_email_switch()
        self.set_themes_switch()

    def close_modal(self) -> None:
        """
        close setting modal
        :return: None
        """
        self.top_level_dialog.destroy()

    def create_top_level_dialog(self) -> None:
        """
        create top level dialog
        :return: None
        """
        self.top_level_dialog = Toplevel(self.master)
        self.top_level_dialog.title(self.title)
        # self.top_level_dialog.minsize(210, 150)
        self.top_level_dialog.maxsize(210, 150)
        self.top_level_dialog.transient(self.master)
        self.top_level_dialog.protocol("WM_DELETE_WINDOW", self.close_modal)

    def set_frame(self) -> None:
        """
        create frame in view. All content will be show in the frame.
        :return: None
        """
        self.main_frame = ttk.LabelFrame(self.top_level_dialog)
        self.main_frame.pack(fill=X, expand=False)

    def set_sms_switch(self):
        """
        sms on/off notification
        :return: None
        """
        self.sms_switch_status = IntVar()

        if self.sms_status == "True":
            self.sms_switch_status.set(0)  # Set switch to ON position
        else:
            self.sms_switch_status.set(1)  # Set switch to OFF position

        switch = ttk.Checkbutton(self.main_frame, text='SMS Notification', style='Switch',
                                 variable=self.sms_switch_status, offvalue=0, onvalue=1,
                                 command=self.on_sms_switch_listener)
        switch.pack(fill=X, expand=False, padx=self.PAD_X, pady=(self.PAD_Y, 0))
        switch.invoke()

    def on_sms_switch_listener(self) -> None:
        """
        send data to setting controller according switch status
        :return:
        """
        if self.sms_switch_status.get():
            SettingsController().set_sms_config(True)
        else:
            SettingsController().set_sms_config(False)

    def set_email_switch(self) -> None:
        """
        email on/off notifications
        :return: None
        """
        self.email_switch_status = IntVar()

        if self.email_status == "True":
            self.email_switch_status.set(0)  # Set switch to ON position
        else:
            self.email_switch_status.set(1)  # Set switch to OFF position

        switch = ttk.Checkbutton(self.main_frame, text='EMAIL Notification', style='Switch',
                                 variable=self.email_switch_status, offvalue=0, onvalue=1,
                                 command=self.on_email_switch_listener)
        switch.pack(fill=X, expand=False, padx=self.PAD_X, pady=(self.PAD_Y, 0))
        switch.invoke()

    def on_email_switch_listener(self) -> None:
        """
        send data to setting controller according switch status
        :return: None
        """
        if self.email_switch_status.get():
            SettingsController().set_email_config(True)
        else:
            SettingsController().set_email_config(False)

    def set_themes_switch(self) -> None:
        """
        Customize theme switch
        :return: None
        """
        self.theme_switch_status = IntVar()

        if self.app_theme == self.night_theme:
            self.theme_switch_status.set(0)  # Set switch to OFF position
        else:
            self.theme_switch_status.set(1)  # Set switch to ON position

        switch = ttk.Checkbutton(self.main_frame, text='Night Theme', style='Switch',
                                 variable=self.theme_switch_status, offvalue=0, onvalue=1,
                                 command=self.on_theme_switch_listener)
        switch.pack(fill=X, expand=False, padx=self.PAD_X, pady=self.PAD_Y)
        switch.invoke()

    def on_theme_switch_listener(self) -> None:
        """
        called when theme switch changed
        :return: None
        """
        if self.theme_switch_status.get():
            SettingsController().set_theme(self.night_theme)
        else:
            SettingsController().set_theme(self.day_theme)
