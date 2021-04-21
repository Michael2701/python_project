from App.Models.GeneticFileModel import GeneticFileModel


class GeneticFileMigration:
    def __init__(self):
        super().__init__()
        self.create_files_table()
        self.insert_dummy_file()

    @staticmethod
    def create_files_table() -> None:
        try:
            GeneticFileModel.createTable()
        except Exception as e:
            print(str(e))

    @staticmethod
    def insert_dummy_file() -> None:
        try:
            GeneticFileModel._connection.debug = True
            person = GeneticFileModel(user_id="1", file_name="Muhi", file_description="Mnogo muh",
                                      file_created_at="02/04/2021")
        except Exception as e:
            print(str(e))
