#!/usr/bin/python3
"""
Script that lists all cities from the database hbtn_0e_4_usa
Results are sorted in ascending order by cities.id
"""


import sys
import MySQLdb

if __name__ == '__main__':
    conn = MySQLdb.connect(host="localhost", port=3306,
                           user=sys.argv[1], passwd=sys.argv[2],
                           db=sys.argv[3], charset="utf8")
    cur = conn.cursor()
    query = """SELECT cities.id, cities.name, states.name
               FROM cities
               JOIN states ON cities.state_id = states.id
               ORDER BY id ASC"""
    cur.execute(query)
    for row in cur.fetchall():
        print(row)
    cur.close()
    conn.close()
