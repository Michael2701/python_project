from App.Models.GeneticFileModel import GeneticFileModel


class GeneticFileMigration:
    """
    create files table and insert one dummy file
    """
    def __init__(self):
        self.create_files_table()
        self.insert_dummy_file()

    def create_files_table(self) -> None:
        """
        create files table
        :return: None
        """
        try:
            GeneticFileModel.createTable()
        except Exception as e:
            print(str(e))

    def insert_dummy_file(self) -> None:
        """
        insert one dummy file
        :return: None
        """
        try:
            # GeneticFileModel._connection.debug = True
            GeneticFileModel(user_id="1", file_name="Muhi", file_description="Mnogo muh",
                             file_created_at="02/04/2021")
        except Exception as e:
            print(str(e))
