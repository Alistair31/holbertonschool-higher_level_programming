# Python - Inheritance

## Concepts clés

### Héritage

L'**héritage** permet à une classe (enfant) d'hériter des attributs et méthodes d'une autre classe (parent), et de les étendre ou redéfinir.

```python
class Animal:
    def speak(self):
        return "..."

class Dog(Animal):        # Dog hérite de Animal
    def speak(self):      # redéfinition (override)
        return "Woof!"
```

---

### lookup — 0-lookup.py

```python
def lookup(obj):
    return dir(obj)
```

- `dir(obj)` retourne la liste de tous les attributs et méthodes d'un objet.
- Utile pour l'introspection.

---

### Hériter de list — 1-my_list.py

```python
class MyList(list):
    def print_sorted(self):
        print(sorted(self))   # sorted() retourne une nouvelle liste triée
```

- `MyList` hérite de `list` : elle a toutes les méthodes de `list` plus `print_sorted`.
- `sorted(self)` : retourne une **nouvelle liste** triée sans modifier `self`.

---

### isinstance vs type

#### is_same_class — 2-is_same_class.py

```python
def is_same_class(obj, a_class):
    return type(obj) is a_class
```

- `type(obj) is a_class` : `True` seulement si `obj` est **exactement** de ce type.
- `isinstance(obj, a_class)` : `True` si `obj` est de ce type **ou d'une sous-classe**.

```python
class Animal: pass
class Dog(Animal): pass

dog = Dog()
type(dog) is Dog      # True
type(dog) is Animal   # False ← différence clé
isinstance(dog, Dog)    # True
isinstance(dog, Animal) # True ← hérite de Animal
```

#### is_kind_of_class — 3-is_kind_of_class.py

```python
def is_kind_of_class(obj, a_class):
    return isinstance(obj, a_class)
```

#### inherits_from — 4-inherits_from.py

```python
def inherits_from(obj, a_class):
    return isinstance(obj, a_class) and type(obj) is not a_class
```

Retourne `True` si l'objet est une instance d'une **sous-classe** (pas de la classe elle-même).

---

### super() — Appeler le parent

```python
class Rectangle(BaseGeometry):
    def __init__(self, width, height):
        self.integer_validator("width", width)   # méthode héritée
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height

    def area(self):
        return self.__width * self.__height
```

```python
super().__init__(args)   # appeler le __init__ du parent
super().methode()         # appeler une méthode du parent
```

---

### Lever des exceptions pour valider — 7-base_geometry.py

```python
class BaseGeometry:
    def area(self):
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        if type(value) is not int:
            raise TypeError(f"{name} must be an integer")
        if value <= 0:
            raise ValueError(f"{name} must be greater than 0")
```

- Lever `Exception` pour une méthode non implémentée simule une méthode abstraite.
- `integer_validator` est réutilisable par toutes les sous-classes.

---

### `__str__` dans les sous-classes

```python
class Rectangle(BaseGeometry):
    def __str__(self):
        return f"[Rectangle] {self.__width}/{self.__height}"
```

---

### Arbre d'héritage de Python

Toutes les classes héritent implicitement de `object` :

```python
class MyClass:
    pass
# équivalent à :
class MyClass(object):
    pass
```

```python
object.__mro__   # (object,)
MyList.__mro__   # (MyList, list, object)
```

---

## Résumé des fichiers

| Fichier | Concept principal |
|---------|-------------------|
| `0-lookup.py` | `dir()`, introspection |
| `1-my_list.py` | Hériter de `list`, ajouter une méthode |
| `2-is_same_class.py` | `type(obj) is a_class` |
| `3-is_kind_of_class.py` | `isinstance()` |
| `4-inherits_from.py` | Sous-classe stricte |
| `5-base_geometry.py` | Classe vide avec `pass` |
| `6-base_geometry.py` | Méthode qui lève une exception |
| `7-base_geometry.py` | Validateur entier avec TypeError/ValueError |
| `10-square.py` | Rectangle → Square, héritage en chaîne |
| `11-square.py` | `__str__` dans une sous-classe |
