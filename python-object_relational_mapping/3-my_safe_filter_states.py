#!/usr/bin/python3
"""
This script tests for SQL injection vulnerabilities in a MySQL database.
It connects to the database using provided credentials and executes
a parameterized query to retrieve states with a specific name.
The results are printed to the console.
The script also handles potential database errors and ensures that
the database connection is properly closed after execution.
"""
import MySQLdb
import sys


def test_injection():
    """Tests for SQL injection vulnerabilities."""
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
                    "WHERE name = %s"
                    "ORDER BY id ASC", (state_name,))

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
    test_injection()
