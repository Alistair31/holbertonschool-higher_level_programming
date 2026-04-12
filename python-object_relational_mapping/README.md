# Python - Object-Relational Mapping (ORM)

## Concepts clés

### Qu'est-ce que l'ORM ?

Un **ORM** (Object-Relational Mapper) fait correspondre des tables de base de données à des **classes Python**. Plutôt qu'écrire du SQL brut, on manipule des objets Python.

Ce projet couvre deux approches :
1. **MySQLdb** : connexion directe avec SQL brut
2. **SQLAlchemy** : ORM complet

---

### MySQLdb — SQL brut — 0-select_states.py

```python
import MySQLdb, sys

db = MySQLdb.connect(
    host="localhost", port=3306,
    user=sys.argv[1], passwd=sys.argv[2], db=sys.argv[3]
)
cur = db.cursor()
cur.execute("SELECT * FROM states ORDER BY id ASC")
rows = cur.fetchall()
for row in rows:
    print(row)
cur.close()
db.close()
```

**Flux :** `connect()` → `cursor()` → `execute()` → `fetchall()` → `close()`

---

### Injection SQL et requêtes paramétrées — 2-my_filter_states.py

**DANGER — injection SQL :**
```python
# NE PAS FAIRE :
cur.execute(f"SELECT * FROM states WHERE name = '{name}'")
```

**Solution — paramètres liés :**
```python
cur.execute("SELECT * FROM states WHERE name = %s", (name,))
```

Les paramètres sont passés séparément : MySQLdb les échappe automatiquement.

---

### SQLAlchemy — ORM

Définir une table comme classe Python :

```python
from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class State(Base):
    __tablename__ = 'states'
    id   = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(128), nullable=False)
```

**CRUD avec SQLAlchemy :**

```python
engine  = create_engine('mysql+mysqldb://user:pass@localhost/db')
Session = sessionmaker(bind=engine)
session = Session()

# CREATE
session.add(State(name="California"))
session.commit()

# READ
states = session.query(State).order_by(State.id).all()

# UPDATE
state = session.query(State).filter_by(id=2).first()
state.name = "New York"
session.commit()

# DELETE
session.delete(session.query(State).filter_by(id=5).first())
session.commit()
```

---

### Jointures — 14-model_city_fetch_by_state.py

```python
results = session.query(State, City)\
                  .filter(City.state_id == State.id)\
                  .order_by(City.id).all()
for state, city in results:
    print(f"{state.name}: ({city.id}) {city.name}")
```

---

## Résumé des fichiers

| Fichier | Concept principal |
|---------|-------------------|
| `0-select_states.py` | MySQLdb, `connect()`, `cursor()`, `fetchall()` |
| `1-filter_states.py` | `WHERE` en SQL brut |
| `2-my_filter_states.py` | Requêtes paramétrées, anti-injection SQL |
| `10-model_state_my_get.py` | SQLAlchemy, `.filter_by()`, `.first()` |
| `11-model_state_insert.py` | `session.add()`, `commit()` |
| `12-model_state_update_id_2.py` | Mise à jour via SQLAlchemy |
| `13-model_state_delete_a.py` | `session.delete()` |
| `14-model_city_fetch_by_state.py` | Jointure deux tables |
