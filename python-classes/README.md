# Python - Classes and Objects

## Concepts clés

### La Programmation Orientée Objet (POO)

La POO organise le code autour d'**objets** qui combinent données (attributs) et comportements (méthodes).

- **Classe** : le modèle / le plan de construction.
- **Objet (instance)** : une réalisation concrète de la classe.

---

### Définir une classe — 0-square.py

```python
class Square:
    pass
```

La classe la plus simple — elle ne fait rien mais est valide.

---

### `__init__` — le constructeur — 1-square.py

```python
class Square:
    def __init__(self, size):
        self.__size = size
```

- `__init__` est appelé automatiquement à la création d'une instance.
- `self` représente l'instance courante.
- `self.__size` : attribut **privé** (name mangling — renommé `_Square__size`).

---

### Validation dans `__init__` — 2-square.py

```python
def __init__(self, size=0):
    if not isinstance(size, int):
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")
    self.__size = size
```

- `isinstance(size, int)` vérifie le type.
- `raise TypeError(...)` lève une exception si le type est incorrect.
- `raise ValueError(...)` lève une exception si la valeur est incorrecte.

---

### Méthodes d'instance — 3-square.py

```python
def area(self):
    return self.__size * self.__size
```

- Toutes les méthodes prennent `self` en premier paramètre.
- `area()` retourne la surface du carré.

---

### @property — Getters et Setters — 4-square.py

```python
@property
def size(self):
    return self.__size      # getter : accessible via obj.size

@size.setter
def size(self, value):
    if not isinstance(value, int):
        raise TypeError("size must be an integer")
    if value < 0:
        raise ValueError("size must be >= 0")
    self.__size = value     # setter : assigner via obj.size = 5
```

**Utilisation :**
```python
sq = Square(4)
print(sq.size)    # 4  (getter)
sq.size = 7       # (setter avec validation)
print(sq.area())  # 49
```

---

### `__str__` et `__repr__` — 6-square.py

```python
def __str__(self):
    if self.__size == 0:
        return ""
    return "\n".join(["#" * self.__size] * self.__size)
```

- `__str__` définit la représentation lisible de l'objet (utilisée par `print()`).
- `__repr__` définit la représentation officielle (utilisée dans le shell interactif).

**Afficher un carré 3×3 :**
```
###
###
###
```

---

### Encapsulation

| Préfixe | Convention | Accès |
|---------|-----------|-------|
| `name` | Public | Accessible partout |
| `_name` | Protégé | Convention : usage interne |
| `__name` | Privé | Name mangling : `_ClassName__name` |

---

### Méthodes spéciales (dunder methods)

| Méthode | Déclenchée par |
|---------|----------------|
| `__init__` | `Square()` |
| `__str__` | `print(obj)` ou `str(obj)` |
| `__repr__` | `repr(obj)` |
| `__del__` | `del obj` |
| `__eq__` | `obj1 == obj2` |
| `__lt__` | `obj1 < obj2` |

---

## Résumé des fichiers

| Fichier | Concept principal |
|---------|-------------------|
| `0-square.py` | Classe vide, syntaxe de base |
| `1-square.py` | `__init__`, attribut privé |
| `2-square.py` | Validation avec `isinstance`, `raise` |
| `3-square.py` | Méthode `area()` |
| `4-square.py` | `@property` getter et setter |
| `5-square.py` | Méthode `my_print()` avec `#` |
| `6-square.py` | `__str__`, position d'affichage |
