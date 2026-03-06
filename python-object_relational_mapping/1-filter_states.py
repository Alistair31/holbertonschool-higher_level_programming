#!/usr/bin/python3
"""
This script connects to a MySQL database and retrieves all
states from the 'states' table where the name starts with 'N'.
The results are ordered by the state ID in ascending order.
The database connection parameters (username, password, and database name)
"""
import MySQLdb
import sys


def list_n_states():
    """Lists all states from the database hbtn_0e_0_usa."""
    username = sys.argv[1]
    password = sys.argv[2]
    db_name = sys.argv[3]

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
                    "WHERE name LIKE 'N%' ORDER BY id ASC")

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
    list_n_states()
