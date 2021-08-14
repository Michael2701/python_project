from App.Models.InterferenceModel import InterferenceModel


class InterferenceMigration:
    """
    create interference table
    """
    def __init__(self):
        self.create_intreference_table()

    def create_intreference_table(self) -> None:
        """
        create interference table
        :return: None
        """
        try:
            InterferenceModel.createTable()
        except Exception as e:
            print(str(e))
