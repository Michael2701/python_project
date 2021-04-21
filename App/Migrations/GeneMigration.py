from App.Models.GeneModel import GeneModel


class GeneMigration:
    def __init__(self):
        """
        create genes table and fill it with one dummy gene
        """
        self.create_genes_table()
        self.insert_dummy_gene()

    def create_genes_table(self) -> None:
        """
        create genes table
        :return: None
        """
        try:
            GeneModel.createTable()

        except Exception as e:
            print(str(e))

    def insert_dummy_gene(self) -> None:
        """
        insert one dummy gene
        :return: None
        """
        try:
            # GeneModel._connection.debug = True
            GeneModel(file_id="3", name="gene1", distance="123", successors="321")
        except Exception as e:
            print(str(e))
