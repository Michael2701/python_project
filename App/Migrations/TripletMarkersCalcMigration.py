from App.Models.TripletMarkersCalc import TripletMarkersCalc


class TripletMarkersCalcMigration:
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
            TripletMarkersCalc.createTable()

        except Exception as e:
            print(str(e))

