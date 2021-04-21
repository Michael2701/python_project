import json
from App.Controllers.Controller import Controller

class SettingsController(Controller):

    config_path = "App/config.json"


    def set_view_settings(self, view) -> None:
        with open(self.config_path) as json_config:
            
            config = json.load(json_config)
            
            view.bg = config['background_color']
            view.bg_modal = config['modal_bg']
            view.fg = config['font_color']
            view.title_font = config['title_font']
            view.font = config['app_font']


    def set_config(self, config):
        pass