#!/usr/bin/python3
"""print all states with a name starting with N (upper N) from the database"""


import MySQLdb as sql
from sys import argv

if __name__ == '__main__':

    state_name = argv[4]

    db = sql.connect(host="localhost",
                     port=3306, user=argv[1], passwd=argv[2], db=argv[3], state_name=argv[4])
    cur = db.cursor()
    query = "SELECT * FROM states WHERE name = '{}' ORDER BY id ASC".format(state_name)
    rows = cur.fetchall(query)
    for row in rows:
        print(row)

