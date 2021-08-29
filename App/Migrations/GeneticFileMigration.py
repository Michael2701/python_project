from App.Models.GeneticFileModel import GeneticFileModel


class GeneticFileMigration:
    """
    create files table and insert one dummy file
    """
    def __init__(self):
        self.create_files_table()

    def create_files_table(self) -> None:
        """
        create files table
        :return: None
        """
        try:
            GeneticFileModel.createTable()
        except Exception as e:
            print(str(e))

