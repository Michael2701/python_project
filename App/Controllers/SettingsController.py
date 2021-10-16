import json
from typing import Any
from App.Controllers.Controller import Controller


class SettingsController(Controller):

    # config_path = "App/config.json"
    config_path = "/home/ty/PycharmProjects/python_project/App/config.json"

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

    def set_notifications_config(self, config: dict) -> None:
        """
        save do json file configuration
        :param config: sms_status & email_status
        :return: None
        """
        # self.set_sms_config(config['sms_status'])
        # self.set_email_config(config['email_status'])

    def get_sms_notification_status(self) -> str:
        """
        get status on/off of sms notification in config file
        :return: true if active otherwise false
        """
        with open(self.config_path) as json_config:
            config = json.load(json_config)
            return config['sms_notification']

    def get_email_notification_status(self) -> str:
        """
        get status on/off of email notification in config file
        :return: true if active otherwise false
        """
        with open(self.config_path) as json_config:
            config = json.load(json_config)
            return config['email_notification']

    def set_sms_config(self, is_sms_notification_active: bool) -> None:
        """
        set status on/off of sms notification in config file
        :param is_sms_notification_active: tue if notification is active otherwise false
        :return: None
        """
        with open(self.config_path) as json_config:
            config = json.load(json_config)

        with open(self.config_path, 'w') as json_config:
            config['sms_notification'] = str(is_sms_notification_active)
            json.dump(config, json_config)

    def set_email_config(self, is_email_notification_active: bool) -> None:
        """
        set status on/off of email notification in config file
        :param is_email_notification_active: 1 true notification is active otherwise false
        :return: None
        """
        with open(self.config_path) as json_config:
            config = json.load(json_config)

        with open(self.config_path, 'w') as json_config:
            config['email_notification'] = str(is_email_notification_active)
            json.dump(config, json_config)

    def get_theme_path(self) -> str:
        """
        get theme path
        :return: path to theme
        """
        with open(self.config_path) as json_config:
            config = json.load(json_config)
            return config['theme']

    def set_theme(self, theme_path: str) -> None:
        """
        save theme path to json config file. Help switch themes
        :param theme_path: path to theme in project
        :return: None
        """
        with open(self.config_path) as json_config:
            config = json.load(json_config)

        with open(self.config_path, 'w') as json_config:
            config['theme'] = theme_path
            json.dump(config, json_config)
