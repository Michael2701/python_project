""" This class help upload interference data to data base.

    This class called from back_from_C.py file after C file execution.
"""

import os
import re
import sys
from datetime import datetime

import App.Models.SQLiteConnector
import App.Services.UserNotificator
import App.Controllers.Controller


class InterferenceCreator:
    def __init__(self):
        self.save_interference()
        self.send_notifications()

    def save_interference(self) -> None:
        """
        save interference data to data base.
        :return: None
        """
        connection = App.Models.SQLiteConnector.SQLiteConnector.create_connection('App/DB/project.db')
        field_names = []
        args = sys.argv[1:]

        if len(args) >= 2 and os.path.exists(args[0]):
            query = f"INSERT INTO interference (file_id, step, min_distance, max_distance, timestamp) VALUES(?,?,?,?,?);"
            cur = connection.cursor()
            cur.execute(query, (args[1], args[2], args[3], args[4], datetime.now().strftime("%d/%m/%Y"),))
            connection.commit()
            interference_id = cur.lastrowid
            with(open(args[0])) as file:
                for i, line in enumerate(file):
                    if i == 0:
                        line = line.replace("(", "_").lower()
                        line = re.sub('[ )=]', "", line)
                        field_names = line
                    else:
                        line = "'" + line.replace(",", "','") + "'"
                        query = f"INSERT INTO interference_row (interference_id, {field_names}) VALUES({interference_id},{line});"
                        cur = connection.cursor()
                        cur.execute(query)
                        connection.commit()

            connection.close()

    def send_notifications(self) -> None:
        """
        call to User Notificator class.
        :return: None
        """
        App.Services.UserNotificator.UserNotificator.send_notification("Hi, calculation in Genetic App completed",
                                                                       App.Controllers.Controller.Controller()
                                                                       .get_logged_user()['email'])
