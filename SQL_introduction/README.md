# SQL - Introduction

## Concepts clés

### Qu'est-ce que SQL ?

**SQL** (Structured Query Language) est le langage standard pour gérer des bases de données relationnelles. MySQL, PostgreSQL, SQLite utilisent tous SQL (avec des variantes).

---

### Les bases de données et tables

Une **base de données** contient des **tables**. Une table est une grille de données avec :
- Des **colonnes** (champs) — les types de données.
- Des **lignes** (enregistrements) — les données réelles.

---

### Commandes de base de données

```sql
-- Lister les bases de données
SHOW DATABASES;

-- Créer une base
CREATE DATABASE IF NOT EXISTS my_db;

-- Sélectionner une base pour travailler
USE my_db;

-- Supprimer une base
DROP DATABASE IF EXISTS my_db;
```

---

### Créer une table — 4-first_table.sql

```sql
CREATE TABLE IF NOT EXISTS first_table (
    id   INT,
    name VARCHAR(256)
);
```

**Types courants :**

| Type | Description |
|------|-------------|
| `INT` | Entier |
| `VARCHAR(n)` | Chaîne de max n caractères |
| `TEXT` | Texte long |
| `FLOAT` | Nombre décimal |
| `BOOLEAN` | Vrai/Faux |
| `DATE` | Date (YYYY-MM-DD) |
| `DATETIME` | Date + heure |

```sql
-- Afficher la structure d'une table
DESCRIBE first_table;

-- Afficher la définition complète
SHOW CREATE TABLE first_table;
```

---

### Insérer des données — 7-insert_value.sql

```sql
INSERT INTO first_table (id, name)
VALUES (89, 'Best School');

-- Insérer plusieurs lignes
INSERT INTO first_table (id, name)
VALUES (1, 'Alice'), (2, 'Bob'), (3, 'Charlie');
```

---

### Lire des données — SELECT

```sql
-- Tout sélectionner
SELECT * FROM first_table;

-- Colonnes spécifiques
SELECT id, name FROM first_table;

-- Avec condition
SELECT * FROM first_table WHERE id = 89;

-- Trier
SELECT * FROM second_table ORDER BY score DESC;

-- Limiter le nombre de résultats
SELECT * FROM second_table LIMIT 5;
```

---

### Modifier et supprimer

```sql
-- Modifier
UPDATE first_table
SET name = 'New Name'
WHERE id = 89;

-- Supprimer des lignes
DELETE FROM first_table WHERE id = 89;

-- Vider une table
TRUNCATE TABLE first_table;

-- Supprimer une table
DROP TABLE IF EXISTS first_table;
```

---

### Fonctions d'agrégation — 14-average.sql

```sql
-- Moyenne
SELECT AVG(score) AS average FROM second_table;

-- Somme, Min, Max, Compte
SELECT SUM(score), MIN(score), MAX(score), COUNT(*) FROM second_table;
```

---

### GROUP BY — 15-groups.sql

```sql
-- Compter le nombre d'enregistrements par score
SELECT score, COUNT(*) AS number
FROM second_table
GROUP BY score
ORDER BY score DESC;
```

`GROUP BY` regroupe les lignes ayant la même valeur dans une colonne.

---

### WHERE vs HAVING

- `WHERE` : filtre les lignes **avant** le regroupement.
- `HAVING` : filtre les groupes **après** `GROUP BY`.

```sql
-- Scores > 5 avec plusieurs enregistrements
SELECT score, COUNT(*) AS number
FROM second_table
GROUP BY score
HAVING COUNT(*) > 1;
```

---

## Résumé des fichiers

| Fichier | Concept principal |
|---------|-------------------|
| `0-list_databases.sql` | `SHOW DATABASES` |
| `1-create_database_if_missing.sql` | `CREATE DATABASE IF NOT EXISTS` |
| `2-remove_database.sql` | `DROP DATABASE IF EXISTS` |
| `3-list_tables.sql` | `SHOW TABLES` |
| `4-first_table.sql` | `CREATE TABLE IF NOT EXISTS` |
| `5-full_table.sql` | `DESCRIBE`, `SHOW CREATE TABLE` |
| `6-list_values.sql` | `SELECT *` |
| `7-insert_value.sql` | `INSERT INTO ... VALUES` |
| `10-top_score.sql` | `ORDER BY score DESC` |
| `11-best_score.sql` | `WHERE score >= 10` |
| `14-average.sql` | `AVG()` |
| `15-groups.sql` | `GROUP BY`, `COUNT(*)` |
| `16-no_link.sql` | Filtrer les enregistrements sans nom |
