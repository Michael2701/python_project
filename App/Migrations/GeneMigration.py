from App.Models.GeneModel import GeneModel


class GeneMigration:
    def __init__(self):
        """
        create genes table and fill it with one dummy gene
        """
        self.create_genes_table()

    def create_genes_table(self) -> None:
        """
        create genes table
        :return: None
        """
        try:
            GeneModel.createTable()

        except Exception as e:
            print(str(e))

