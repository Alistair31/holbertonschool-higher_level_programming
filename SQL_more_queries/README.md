# SQL - More Queries

## Concepts clés

### Gestion des utilisateurs — 0-privileges.sql

```sql
-- Créer un utilisateur
CREATE USER IF NOT EXISTS 'user_0d_1'@'localhost' IDENTIFIED BY 'user_0d_1_pwd';

-- Accorder des privilèges
GRANT ALL PRIVILEGES ON *.* TO 'user_0d_1'@'localhost';
GRANT SELECT ON my_db.* TO 'user_0d_2'@'localhost';

-- Afficher les privilèges
SHOW GRANTS FOR 'user_0d_1'@'localhost';

-- Révoquer des privilèges
REVOKE SELECT ON my_db.* FROM 'user_0d_2'@'localhost';
```

---

### Contraintes (Constraints)

Les contraintes garantissent l'intégrité des données.

#### PRIMARY KEY

```sql
CREATE TABLE states (
    id   INT NOT NULL UNIQUE AUTO_INCREMENT,
    name VARCHAR(256) NOT NULL,
    PRIMARY KEY (id)
);
```

- `PRIMARY KEY` : identifiant unique de chaque ligne.
- `AUTO_INCREMENT` : incrémentation automatique à chaque insertion.
- `NOT NULL` : la colonne ne peut pas être vide.
- `UNIQUE` : pas de doublons.

#### FOREIGN KEY

```sql
CREATE TABLE cities (
    id       INT NOT NULL AUTO_INCREMENT,
    state_id INT NOT NULL,
    name     VARCHAR(256) NOT NULL,
    PRIMARY KEY (id),
    FOREIGN KEY (state_id) REFERENCES states(id)
);
```

- La `FOREIGN KEY` garantit que `state_id` existe bien dans la table `states`.
- Empêche les données orphelines.

---

### Jointures (JOINs)

Les jointures combinent des lignes de plusieurs tables.

#### INNER JOIN — 10-genre_id_by_show.sql

```sql
SELECT tv_shows.title, tv_show_genres.genre_id
FROM tv_shows
JOIN tv_show_genres ON tv_shows.id = tv_show_genres.show_id
ORDER BY tv_shows.title, tv_show_genres.genre_id;
```

- `INNER JOIN` (ou `JOIN`) : retourne seulement les lignes avec correspondance dans **les deux** tables.

#### LEFT JOIN — 11-genre_id_all_shows.sql

```sql
SELECT tv_shows.title, tv_show_genres.genre_id
FROM tv_shows
LEFT JOIN tv_show_genres ON tv_shows.id = tv_show_genres.show_id
ORDER BY tv_shows.title;
```

- `LEFT JOIN` : retourne **toutes** les lignes de la table de gauche, même sans correspondance (NULL pour les colonnes de droite).

#### Schéma des jointures

```
INNER JOIN : A ∩ B
LEFT JOIN  : A + (A ∩ B)
RIGHT JOIN : B + (A ∩ B)
FULL JOIN  : A ∪ B
```

---

### Jointures multiples — 16-shows_by_genre.sql

```sql
SELECT tv_genres.name AS name
FROM tv_genres
JOIN tv_show_genres ON tv_genres.id = tv_show_genres.genre_id
JOIN tv_shows ON tv_show_genres.show_id = tv_shows.id
WHERE tv_shows.title = 'Dexter'
ORDER BY name;
```

**Lecture :** 
1. Partir de `tv_genres`
2. Joindre `tv_show_genres` via `genre_id`
3. Joindre `tv_shows` via `show_id`
4. Filtrer sur le titre

---

### Sous-requêtes (Subqueries)

```sql
-- Séries sans genre
SELECT tv_shows.title
FROM tv_shows
WHERE tv_shows.id NOT IN (
    SELECT show_id FROM tv_show_genres
)
ORDER BY title;
```

---

### Tables de liaison (Many-to-Many)

Un show peut avoir plusieurs genres, et un genre peut appartenir à plusieurs shows → table de liaison :

```
tv_shows ←─ tv_show_genres ─→ tv_genres
  id                              id
  title    show_id, genre_id      name
```

---

## Résumé des fichiers

| Fichier | Concept principal |
|---------|-------------------|
| `0-privileges.sql` | `SHOW GRANTS`, utilisateurs MySQL |
| `1-create_user.sql` | `CREATE USER`, `GRANT ALL PRIVILEGES` |
| `2-create_read_user.sql` | `GRANT SELECT` seulement |
| `3-force_name.sql` | `NOT NULL` constraint |
| `4-never_empty.sql` | `DEFAULT` value |
| `5-unique_id.sql` | `UNIQUE` constraint |
| `6-states.sql` | `PRIMARY KEY`, `AUTO_INCREMENT` |
| `7-cities.sql` | `FOREIGN KEY`, `REFERENCES` |
| `10-genre_id_by_show.sql` | `INNER JOIN` |
| `11-genre_id_all_shows.sql` | `LEFT JOIN` |
| `12-no_genre.sql` | `LEFT JOIN` + `WHERE IS NULL` |
| `13-count_shows_by_genre.sql` | `COUNT`, `GROUP BY` |
| `14-my_genres.sql` | `JOIN` multiple |
| `15-comedy_only.sql` | Filtrer par genre |
| `16-shows_by_genre.sql` | Triple jointure |
