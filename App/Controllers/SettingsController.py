import json
from typing import Any
from App.Controllers.Controller import Controller


class SettingsController(Controller):

    config_path = "App/config.json"

    def set_view_settings(self, view: Any) -> None:
        """
        set view style variables in given view
        :param view: view to set style variables
        :return: None
        """
        with open(self.config_path) as json_config:
            config = json.load(json_config)
            
            view.bg = config['background_color']
            view.bg_modal = config['modal_bg']
            view.fg = config['font_color']
            view.title_font = config['title_font']
            view.font = config['app_font']

    def set_notification_config(self, config: dict):
        """
        save do json file configuration
        :param config:
        :return:
        """
        print("Warning: set_notification_config NOT IMPLEMENTED")

    def get_sms_config(self) -> int:
        """
        get status on/off of sms notification in config file
        :return: 1 if on otherwise 0
        """
        with open(self.config_path) as json_config:
            config = json.load(json_config)
            return int(config['sms_notification'])

    def get_email_config(self) -> int:
        """
        get status on/off of email notification in config file
        :return: 1 if on otherwise 0
        """
        with open(self.config_path) as json_config:
            config = json.load(json_config)
            return int(config['email_notification'])

    def set_sms_config(self, sms_status: int) -> None:
        """
        set status on/off of sms notification in config file
        :param sms_status: 1 if notification is on otherwise 0
        :return: None
        """
        with open(self.config_path) as json_config:
            config = json.load(json_config)
            config['sms_notification'] = str(sms_status)

    def set_email_config(self, email_status: int) -> None:
        """
        set status on/off of email notification in config file
        :param email_status: 1 if notification is on otherwise 0
        :return: None
        """
        with open(self.config_path) as json_config:
            config = json.load(json_config)
            config['email_notification'] = str(email_status)
