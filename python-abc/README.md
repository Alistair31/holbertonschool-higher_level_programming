# Python - Abstract Classes, Interfaces and Subclassing

## Concepts clés

### Classes abstraites (ABC)

Une **classe abstraite** définit une interface — un contrat que les sous-classes doivent respecter. On ne peut pas instancier une classe abstraite directement.

```python
from abc import ABC, abstractmethod

class Animal(ABC):
    @abstractmethod
    def sound(self):
        pass   # les sous-classes DOIVENT implémenter cette méthode
```

- `ABC` : classe de base pour les classes abstraites (du module `abc`).
- `@abstractmethod` : décorateur qui rend une méthode obligatoire à implémenter.

---

### Implémenter une classe abstraite — task_00_abc.py

```python
class Dog(Animal):
    def sound(self):
        return "Bark"

class Cat(Animal):
    def sound(self):
        return "Meow"
```

- `Dog` et `Cat` **héritent** de `Animal` et implémentent `sound()`.
- Tenter d'instancier `Animal()` directement lèverait une `TypeError`.

---

### Duck Typing — task_01_duck_typing.py

Le **duck typing** est un concept Python : si un objet a les méthodes et attributs attendus, il peut être utilisé à la place — peu importe son type réel.

```python
def shape_info(shape):
    print(f"Area: {shape.area()}")
    print(f"Perimeter: {shape.perimeter()}")
```

On peut passer n'importe quel objet ayant `area()` et `perimeter()` — qu'il hérite de `Shape` ou non.

#### Classe abstraite Shape avec propriétés

```python
class Shape(ABC):
    @abstractmethod
    def area(self):
        pass

    @abstractmethod
    def perimeter(self):
        pass

class Circle(Shape):
    def __init__(self, radius):
        self.__radius = radius   # attribut privé (name mangling)

    @property
    def radius(self):
        return self.__radius

    @radius.setter
    def radius(self, value):
        self.__radius = value

    def area(self):
        return pi * (self.__radius ** 2)

    def perimeter(self):
        return 2 * pi * self.__radius
```

- `@property` : transforme une méthode en attribut accessible par `obj.radius`.
- `@radius.setter` : permet d'assigner `obj.radius = valeur`.
- `self.__radius` : attribut **privé** — inaccessible directement de l'extérieur.

---

### VerboseList — task_02_verboselist.py

Sous-classe de `list` qui affiche des messages lors des modifications :

```python
class VerboseList(list):
    def append(self, item):
        print(f"Added [{item}] to the list.")
        super().append(item)   # appel de la méthode parente

    def remove(self, item):
        print(f"Removed [{item}] from the list.")
        super().remove(item)
```

- `super()` appelle la méthode de la classe parente.

---

### CountedIterator — task_03_countediterator.py

Itérateur personnalisé qui compte les éléments itérés :

```python
class CountedIterator:
    def __init__(self, iterable):
        self.iterator = iter(iterable)
        self.count = 0

    def __iter__(self):
        return self

    def __next__(self):
        item = next(self.iterator)
        self.count += 1
        return item
```

- `__iter__` et `__next__` : méthodes spéciales pour créer un objet itérable.

---

### Héritage multiple — task_04_flyingfish.py

Python supporte l'**héritage multiple** :

```python
class FlyingFish(Fish, Bird):
    def swim(self):
        print("The flying fish is swimming!")

    def fly(self):
        print("The flying fish is soaring!")

    def habitat(self):
        print("The flying fish lives both in water and the sky!")
```

#### MRO (Method Resolution Order)

L'ordre dans lequel Python cherche les méthodes lors d'un héritage multiple :

```python
print(FlyingFish.__mro__)
# (<class 'FlyingFish'>, <class 'Fish'>, <class 'Bird'>, <class 'object'>)
```

---

### Mixins — task_05_dragon.py

Un **Mixin** est une classe légère qui apporte un comportement spécifique, sans être une classe principale :

```python
class SwimMixin:
    def swim(self):
        print("The creature swims!")

class FlyMixin:
    def fly(self):
        print("The creature flies!")

class Dragon(SwimMixin, FlyMixin):
    def roar(self):
        print("The dragon roars!")
```

- Les mixins sont utilisés pour **composer** des comportements sans relation d'héritage forte.

---

## Résumé des fichiers

| Fichier | Concept principal |
|---------|-------------------|
| `task_00_abc.py` | `ABC`, `@abstractmethod`, sous-classes concrètes |
| `task_01_duck_typing.py` | Duck typing, `@property`, `@setter`, attributs privés |
| `task_02_verboselist.py` | Héritage de `list`, `super()` |
| `task_03_countediterator.py` | `__iter__`, `__next__`, protocole d'itération |
| `task_04_flyingfish.py` | Héritage multiple, MRO |
| `task_05_dragon.py` | Mixins, composition de comportements |
