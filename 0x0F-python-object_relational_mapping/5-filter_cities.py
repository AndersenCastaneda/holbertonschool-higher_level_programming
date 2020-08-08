#!/usr/bin/python3
"""Takes in the name of a state as an argument and lists
all cities of that state, using the database hbtn_0e_4_usa"""


if __name__ == "__main__":
    import MySQLdb
    import sys

    argv = sys.argv
    argc = len(argv)
    if argc == 5:
        db = MySQLdb.connect(host="localhost", port=3306,
                             user=argv[1], passwd=argv[2], db=argv[3])
        cur = db.cursor()
        cur.execute("SELECT cities.name FROM cities, states WHERE states.name = %s AND cities.state_id = states.id", (argv[4],))
        rows = cur.fetchall()
        for i in range(len(rows)):
            if i < len(rows) - 1:
                print(rows[i][0], end=', ')
            else:
                print(rows[i][0])

        cur.close()
        db.close()
