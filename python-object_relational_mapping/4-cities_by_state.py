#!/usr/bin/python3
"""
Lists all City objects from the database hbtn_0e_14_usa
"""
import MySQLdb
import sys


def cities_by_state():
    """Lists all City objects from the database hbtn_0e_14_usa"""

    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]

    try:
        db = MySQLdb.connect(
            host="localhost",
            port=3306,
            user=username,
            passwd=password,
            db=database
        )
        cur = db.cursor()
        cur.execute(
            "SELECT cities.id, cities.name, states.name "
            "FROM cities JOIN states ON cities.state_id = states.id "
            "ORDER BY cities.id ASC"
        )

        rows = cur.fetchall()

        for row in rows:
            print(row)

    except MySQLdb.Error as e:
        print(f"Error: {e}")

    finally:
        if 'cur' in locals():
            cur.close()
        if 'db' in locals():
            db.close()


if __name__ == "__main__":
    cities_by_state()
