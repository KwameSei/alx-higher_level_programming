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
    cur.execute("""SELECT cities.id, cities.name, states.name
    FROM states
    JOIN cities ON states.id = cities.state_id
    ORDER BY cities.id ASC""")

    rows_query = cur.fetchall()
    for row in rows_query:
        print(row)

    # Closing the cursing
    cur.close()
    # Closing the database
    start_db.close()
