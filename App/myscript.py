import os
import re
import sys
import time
import Models.SQLiteConnector


def save_interference():
    connection = Models.SQLiteConnector.SQLiteConnector.create_connection('App/DB/project.db')
    field_names = []
    args = sys.argv[1:]
    calc_id = int(time.time())

    print(args)
    if len(args) >= 2 and os.path.exists(args[0]):
        with(open(args[0])) as file:
            for i, line in enumerate(file):
                if i == 0:
                    line = line.replace("(", "_").lower()
                    line = re.sub('[ )=]', "", line)
                    field_names = line
                else:
                    line = "'" + line.replace(",", "','") + "'"
                    query = f"INSERT INTO markers_calc ({field_names},file_id, calc_id, step, min_distance, max_distance) VALUES({line},'{args[1]}','{calc_id}','{args[2]}','{args[3]}','{args[4]}');"
                    cur = connection.cursor()
                    cur.execute(query)
                    # print(query)

            # print(os.path.exists('App/DB/project.db'))
    cur = connection.cursor()
    cur.execute("select * from markers_calc")
    print(cur.fetchall())


save_interference()

