#!/usr/bin/python3
"""
This script connects to a MySQL database and retrieves all
states from the 'states' table where the name matches the provided argument.
The results are ordered by the state ID in ascending order.
The database connection parameters (username, password, and database name)
"""
import MySQLdb
import sys


def display_prompted_states():
    """Displays states from the database hbtn_0e_0_usa."""
    username = sys.argv[1]
    password = sys.argv[2]
    db_name = sys.argv[3]
    state_name = sys.argv[4]

    try:
        db = MySQLdb.connect(
            host="localhost",
            port=3306,
            user=username,
            passwd=password,
            db=db_name
        )
        cur = db.cursor()
        cur.execute("SELECT * FROM states "
                    "WHERE name = '{}' "
                    "ORDER BY id ASC".format(state_name))
        query_rows = cur.fetchall()

        for row in query_rows:
            print(row)

    except MySQLdb.Error as e:
        print(f"Error: {e}")

    finally:
        if 'cur' in locals():
            cur.close()
        if 'db' in locals():
            db.close()


if __name__ == "__main__":
    display_prompted_states()
