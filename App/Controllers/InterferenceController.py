from App.Controllers.Controller import Controller
from App.Services.InterferenceCreator import InterferenceCreator


class InterferenceController(Controller):

    def __init__(self):
        pass

    def creat(self):
        InterferenceCreator().count_N_xx()
