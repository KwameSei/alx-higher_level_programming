#!/usr/bin/python3
import MySQLdb
from sys import argv

'''
script that lists all states names beginning with the uppercase N
from database hbtn_0e_0_usa
'''

if __name__ == "__main__":
    start_db = MySQLdb.connect(
            host="localhost",
            port=3306,
            user=argv[1],
            passwd=argv[2],
            db=argv[3],
            charset="utf8"
            )

    cur = start_db.cursor()
    cur.execute("""SELECT * FROM states WHERE name='{}' ORDER by id ASC""".format(argv[4]))

    rows_query = cur.fetchall()
    for row in rows_query:
        print(row)
    cur.close()
    start_db.close()
