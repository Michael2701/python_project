import os
import re
import sys
from datetime import datetime

import Models.SQLiteConnector

print("hi")
def save_interference():
    connection = Models.SQLiteConnector.SQLiteConnector.create_connection('App/DB/project.db')
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


save_interference()
# TODO add trigger send SMS or / and EMAIL

