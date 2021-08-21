import subprocess

from App.Controllers.Controller import Controller
from App.Models.GeneticFileModel import GeneticFileModel
from App.Services.InterferenceCreator import InterferenceCreator


class InterferenceController(Controller):

    def __init__(self):
        pass

    def create(self, file: GeneticFileModel):
        # InterferenceCreator().count_N_xx()
        subprocess.check_call([r"App/Services/c/InterferenceCalculator", "App/file.csv", "fucking shit"])