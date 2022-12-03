#!/usr/bin/python3
'''
Script that lists the state name entered as an argument.
Script is safe from MySQL injections
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
    cur.execute("SELECT * FROM states WHERE name LIKE %s ORDER BY id ASC",
                (argv[4],))

    rows_query = cur.fetchall()
    for row in rows_query:
        print(row)

    # Closing the cursor
    cur.close()
    # Closing the database
    start_db.close()
