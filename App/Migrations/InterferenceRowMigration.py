from App.Models.InterferenceRowModel import InterferenceRowModel


class InterferenceRowMigration:
    def __init__(self):
        """
        create genes table
        """
        self.create_table()

    def create_table(self) -> None:
        """
        create genes table
        :return: None
        """
        try:
            InterferenceRowModel.createTable()

        except Exception as e:
            print(str(e))

