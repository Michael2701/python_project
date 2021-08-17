from App.Models.SQLiteConnector import SQLiteConnector
from App.Models.Model import Model
from sqlobject import *


class GeneModel(Model):
    """
    model for genes table
    """
    # file_id = ForeignKey('GeneticFileModel')
    file_id = StringCol()
    name = StringCol()
    distance = StringCol()
    successors = StringCol()

    class sqlmeta:
        """
        define table name
        """
        table = 'genes'

    @staticmethod
    def get_id_list(gene_id: str, file_id: str, min_dist: str, max_dist: str) -> []:
        """

        :param gene_id: ID of gene (marker)
        :param file_id: ID of file
        :param min_dist: minimal dictation between genes
        :param max_dist: maximum dictation between genes
        :return: Array of gene ID's
        """
        connection = SQLiteConnector.create_connection()
        cur = connection.cursor()
        cur.execute("SELECT id FROM genes " +
                    "WHERE (id IN "
                    "(SELECT id " +
                    "FROM genes g1 " +
                    "WHERE ABS(g1.distance-(SELECT distance FROM genes WHERE id="+str(gene_id)+")) >= " +
                    str(min_dist) + " " +
                    "AND ABS(g1.distance-(SELECT distance FROM genes WHERE id="+str(gene_id)+")) <= " +
                    str(max_dist) + ") " +
                    "OR id="+str(gene_id) + ") " +
                    "AND file_id="+str(file_id) + "")

        rows = cur.fetchall()
        return [row[0] for row in rows]
