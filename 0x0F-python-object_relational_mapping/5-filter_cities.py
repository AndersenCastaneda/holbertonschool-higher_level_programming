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
        cur.execute("SELECT cities.name FROM cities, JOIN states\
                     ON cities.state_id = states.id WHERE states.name\
                     LIKE %s ORDER BY cities.id", (argv[4],))
        rows = cur.fetchall()
        print(", ".join(city[0] for city in rows)

        cur.close()
        db.close()
