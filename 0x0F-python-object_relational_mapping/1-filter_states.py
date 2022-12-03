#!/usr/bin/python3
'''
script that lists all states names beginning with the uppercase N
from database hbtn_0e_0_usa
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
    cur.execute("SELECT id, UPPER(name) FROM states WHERE name LIKE 'N%'")

    rows_query = cur.fetchall()
    for row in rows_query:
        print(row)
    cur.close()
    start_db.close()
