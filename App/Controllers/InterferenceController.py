import subprocess

from App.Controllers.Controller import Controller
from App.Models.GeneticFileModel import GeneticFileModel


class InterferenceController(Controller):
    def __init__(self):
        pass

    def create_interference(self, file: GeneticFileModel):
        subprocess.check_call([r"App/Services/c/InterferenceCalculator", "App/triplet_of_genes.csv", "Interference.csv"])
