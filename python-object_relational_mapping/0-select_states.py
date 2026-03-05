#!/usr/bin/python3
"""
Lists all states from the database hbtn_0e_0_usa.
The script takes 3 arguments: mysql username, mysql password,
and database name.
"""
import MySQLdb
import sys


def list_all_states():
    """Lists all states from the database hbtn_0e_0_usa."""
    # Récupération des arguments via sys.argv
    # sys.argv[0] est le nom du script, 1-3 sont les arguments demandés
    username = sys.argv[1]
    password = sys.argv[2]
    db_name = sys.argv[3]

    try:
        # Connexion à la base de données
        db = MySQLdb.connect(
            host="localhost",
            port=3306,
            user=username,
            passwd=password,
            db=db_name
        )
        cur = db.cursor()

        # Exécution de la requête SQL
        # On sélectionne toutes les colonnes de la table 'states'
        cur.execute("SELECT * FROM states ORDER BY id ASC")

        # Récupération de tous les résultats
        query_rows = cur.fetchall()

        # Affichage ligne par ligne selon le format attendu
        for row in query_rows:
            print(row)

    except MySQLdb.Error as e:
        # MySQLdb utilise 'Error' avec une majuscule
        print(f"Error: {e}")

    finally:
        # On ferme proprement le curseur et la connexion
        if 'cur' in locals():
            cur.close()
        if 'db' in locals():
            db.close()


if __name__ == "__main__":
    list_all_states()
