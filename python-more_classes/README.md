# Python - More Classes and Objects

## Concepts clés

Ce module approfondit la POO Python avec des concepts avancés : attributs de classe, méthodes spéciales, méthodes statiques et de classe.

---

### Attributs de classe vs attributs d'instance

```python
class Rectangle:
    number_of_instances = 0    # attribut de CLASSE — partagé par toutes les instances
    print_symbol = "#"         # attribut de CLASSE

    def __init__(self, width=0, height=0):
        self.__width  = width   # attribut d'INSTANCE — propre à chaque objet
        self.__height = height
        Rectangle.number_of_instances += 1   # compter les créations
```

| | Attribut de classe | Attribut d'instance |
|--|-------------------|---------------------|
| Déclaré | Dans le corps de la classe | Dans `__init__` |
| Partagé | Par toutes les instances | Unique par instance |
| Accès | `Rectangle.number` ou `self.number` | `self.width` |

---

### `__del__` — Destructeur — 5-rectangle.py

```python
def __del__(self):
    Rectangle.number_of_instances -= 1
    print("Bye rectangle...")
```

- Appelé automatiquement quand l'objet est détruit (`del rect` ou fin de vie).
- Utile pour le nettoyage et le suivi du nombre d'instances.

---

### `__repr__` et `__str__` — 7-rectangle.py

```python
def __str__(self):
    if self.__width == 0 or self.__height == 0:
        return ""
    return "\n".join([str(self.print_symbol) * self.__width] * self.__height)

def __repr__(self):
    return f"Rectangle({self.__width}, {self.__height})"
```

- `__str__` : représentation lisible → `print(rect)`.
- `__repr__` : représentation officielle → `repr(rect)` et dans le REPL.
- `eval(repr(rect))` devrait recréer l'objet.

---

### Méthode statique `@staticmethod` — 8-rectangle.py

```python
@staticmethod
def bigger_or_equal(rect_1, rect_2):
    if not isinstance(rect_1, Rectangle):
        raise TypeError("rect_1 must be an instance of Rectangle")
    if rect_1.area() >= rect_2.area():
        return rect_1
    return rect_2
```

- Ne prend **ni `self` ni `cls`** en paramètre.
- N'accède pas aux attributs de l'instance ni de la classe.
- Appelée via `Rectangle.bigger_or_equal(r1, r2)`.

---

### Méthode de classe `@classmethod` — 9-rectangle.py

```python
@classmethod
def square(cls, size=0):
    return cls(size, size)   # crée une instance (Rectangle carré)
```

- Prend `cls` (la classe elle-même) en premier paramètre.
- Peut créer des instances : **factory method**.
- Appelée via `Rectangle.square(5)`.

---

### Méthodes spéciales (dunder methods) complètes

| Méthode | Déclenchée par |
|---------|----------------|
| `__init__` | `Rectangle(w, h)` |
| `__del__` | `del rect` |
| `__str__` | `print(rect)`, `str(rect)` |
| `__repr__` | `repr(rect)`, affichage REPL |
| `__len__` | `len(rect)` |
| `__eq__` | `rect1 == rect2` |
| `__lt__` | `rect1 < rect2` |

---

## Résumé des fichiers

| Fichier | Concept principal |
|---------|-------------------|
| `0-rectangle.py` | Classe vide |
| `1-rectangle.py` | `__init__`, `@property` width et height |
| `2-rectangle.py` | `area()`, `perimeter()` |
| `3-rectangle.py` | `__str__`, affichage avec `#` |
| `4-rectangle.py` | `__repr__`, format `Rectangle(w, h)` |
| `5-rectangle.py` | `__del__`, compteur d'instances |
| `6-rectangle.py` | `number_of_instances` (attribut de classe) |
| `7-rectangle.py` | `print_symbol` (attribut de classe personnalisable) |
| `8-rectangle.py` | `@staticmethod bigger_or_equal` |
| `9-rectangle.py` | `@classmethod square` (factory method) |
