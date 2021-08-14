from App.Models.MarkersModel import MarkersModel


class MarkersMigration:
    """
    create interference table
    """
    def __init__(self):
        self.create_markers_table()

    def create_markers_table(self) -> None:
        """
        create interference table
        :return: None
        """
        try:
            MarkersModel.createTable()
        except Exception as e:
            print(str(e))
