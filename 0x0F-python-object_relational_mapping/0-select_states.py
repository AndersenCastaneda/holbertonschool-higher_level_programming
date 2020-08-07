#!/usr/bin/python3
"""Lists all states from the database hbtn_0e_0_usa"""


if __name__ == "__main__":
    import MySQLdb
    import sys

    argv = sys.argv
    argc = len(argv)

    if argc == 4:
        db = MySQLdb.connect(host="localhost", port=3306,
                             user=argv[1], passwd=argv[2], db=argv[3])
        cur = db.cursor()
        cur.execute("SELECT * FROM states")
        rows = cur.fetchall()
        for row in rows:
            print(row)

        cur.close()
        db.close()
