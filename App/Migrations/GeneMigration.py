from App.Models.GeneModel import GeneModel


class GeneMigration:
    def __init__(self):
        self.create_genes_table()
        self.insert_dummy_gene()

    @staticmethod
    def create_genes_table() -> None:
        try:
            GeneModel.createTable()

        except Exception as e:
            print(str(e))

    @staticmethod
    def insert_dummy_gene() -> None:
        try:
            GeneModel._connection.debug = True
            person = GeneModel(file_id="3", name="gene1", distance="123", successors="321")
        except Exception as e:
            print(str(e))
