#!/usr/bin/python3
'''
script that lists all states from the database hbtn_0e_0_usa
'''

import MySQLdb
from sys import argv

if __name__ == "__main__":
    start_db = MySQLdb.connect(
            host="localhost",
            port=3306,
            user=argv[1],
            passwd=argv[2],
            db=argv[3],
            )

    cur = start_db.cursor()
    cur.execute("""SELECT cities.name FROM cities, states WHERE
    cities.state_id = states.id AND states.name = %s""", (argv[4],))

    rows_query = cur.fetchall()
    # Create new list
    new_list = []
    for row in rows_query:
        new_list.append(row[0])
    print(', '.join(city[0] for city in rows_query))

    # Closing the cursing
    cur.close()
    # Closing the database
    start_db.close()
