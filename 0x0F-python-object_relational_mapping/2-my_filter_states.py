#!/usr/bin/python3
"""Script that takes in an argument and displays all values
in the states table of hbtn_0e_0_usa
where name matches the argument.
"""


import sys
import MySQLdb

if __name__ == '__main__':
    conn = MySQLdb.connect(host="localhost", port=3306,
                           user=sys.argv[1], passwd=sys.argv[2],
                           db=sys.argv[3], charset="utf8")
    cur = conn.cursor()
    query = """SELECT * FROM states
               WHERE name = '{:s}'
               ORDER BY id ASC""".format(sys.argv[4])
    cur.execute(query)
    for row in cur.fetchall():
        if row[1] == sys.argv[4]:
            print(row)
    cur.close()
    conn.close()
