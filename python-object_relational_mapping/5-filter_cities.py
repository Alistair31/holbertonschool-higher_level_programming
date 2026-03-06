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
    state_name = sys.argv[4]

    try:
        db = MySQLdb.connect(
            host="localhost",
            port=3306,
            user=username,
            passwd=password,
            db=database
        )
        cur = db.cursor()
        query = """
        SELECT cities.name
        FROM cities
        JOIN states ON cities.state_id = states.id
        WHERE states.name = %s
        ORDER BY cities.id ASC
        """
        cur.execute(query, (state_name,))
        rows = cur.fetchall()

        # Extraction des noms de villes
        cities = [row[0] for row in rows]

        print(", ".join(cities))

    except MySQLdb.Error as e:
        print(f"Error: {e}")

    finally:
        if 'cur' in locals():
            cur.close()
        if 'db' in locals():
            db.close()


if __name__ == "__main__":
    cities_by_state()
