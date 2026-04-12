# Python - Input / Output

## Concepts clés

### Ouvrir et lire un fichier — 0-read_file.py

```python
def read_file(filename=""):
    with open(filename, "r", encoding="utf-8") as f:
        print(f.read(), end="")
```

- `open(filename, mode, encoding)` : ouvre un fichier.
- `"r"` : mode lecture (read).
- `encoding="utf-8"` : encodage des caractères.
- `with ... as f` : **gestionnaire de contexte** — ferme automatiquement le fichier à la fin du bloc.
- `f.read()` : lit tout le contenu en une fois.

---

### Modes d'ouverture

| Mode | Description |
|------|-------------|
| `"r"` | Lecture (fichier doit exister) |
| `"w"` | Écriture (crée ou vide le fichier) |
| `"a"` | Ajout en fin de fichier |
| `"r+"` | Lecture + écriture |
| `"rb"` | Lecture en mode binaire |

---

### Écrire dans un fichier — 1-write_file.py

```python
def write_file(filename="", text=""):
    with open(filename, "w", encoding="utf-8") as f:
        return f.write(text)   # retourne le nombre de caractères écrits
```

- `f.write(text)` : écrit la chaîne dans le fichier.
- Mode `"w"` : **crée** le fichier s'il n'existe pas, **vide** s'il existe.

### Ajouter à un fichier — 2-append_write.py

```python
with open(filename, "a", encoding="utf-8") as f:
    return f.write(text)
```

- Mode `"a"` : écrit en fin de fichier sans supprimer le contenu existant.

---

### JSON — Sérialisation

#### to_json_string — 3-to_json_string.py

```python
import json

def to_json_string(my_obj):
    return json.dumps(my_obj)   # objet Python → chaîne JSON
```

#### from_json_string — 4-from_json_string.py

```python
def from_json_string(my_str):
    return json.loads(my_str)   # chaîne JSON → objet Python
```

**Correspondance Python ↔ JSON :**

| Python | JSON |
|--------|------|
| `dict` | `object {}` |
| `list` | `array []` |
| `str` | `string ""` |
| `int`, `float` | `number` |
| `True` / `False` | `true` / `false` |
| `None` | `null` |

---

### Sauvegarder/Charger depuis un fichier JSON

#### save_to_json_file — 5-save_to_json_file.py

```python
def save_to_json_file(my_obj, filename):
    with open(filename, "w", encoding="utf-8") as f:
        json.dump(my_obj, f)   # dump = sérialise directement vers un fichier
```

#### load_from_json_file — 6-load_from_json_file.py

```python
def load_from_json_file(filename):
    with open(filename, "r", encoding="utf-8") as f:
        return json.load(f)    # load = désérialise depuis un fichier
```

**Différence `dump`/`dumps` et `load`/`loads` :**
- `dump` / `load` : travaillent avec un **fichier** (file object).
- `dumps` / `loads` : travaillent avec une **chaîne de caractères**.

---

### Triangle de Pascal — 12-pascal_triangle.py

```python
def pascal_triangle(n):
    if n <= 0:
        return []
    triangle = [[1]]
    for i in range(1, n):
        row = [1]
        for j in range(1, i):
            row.append(triangle[i-1][j-1] + triangle[i-1][j])
        row.append(1)
        triangle.append(row)
    return triangle
```

Chaque élément est la somme des deux éléments au-dessus dans la ligne précédente.

---

### Classe Student avec JSON — 10-student.py

```python
class Student:
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name  = last_name
        self.age        = age

    def to_json(self):
        return self.__dict__   # dictionnaire de tous les attributs
```

- `self.__dict__` : dictionnaire `{attribut: valeur}` de l'instance.
- `json.dumps(student.to_json())` sérialise l'objet en JSON.

---

## Résumé des fichiers

| Fichier | Concept principal |
|---------|-------------------|
| `0-read_file.py` | `open()`, `with`, `f.read()` |
| `1-write_file.py` | Mode `"w"`, `f.write()` |
| `2-append_write.py` | Mode `"a"`, ajout en fin |
| `3-to_json_string.py` | `json.dumps()` |
| `4-from_json_string.py` | `json.loads()` |
| `5-save_to_json_file.py` | `json.dump()` vers fichier |
| `6-load_from_json_file.py` | `json.load()` depuis fichier |
| `10-student.py` | `self.__dict__`, sérialisation d'objet |
| `11-student.py` | Filtrage des attributs à sérialiser |
| `12-pascal_triangle.py` | Triangle de Pascal, liste de listes |
