# Python - Data Structures: Lists, Tuples

## Concepts clés

### Les listes (list)

Une **liste** est une collection ordonnée, **mutable** (modifiable), d'éléments de types quelconques.

```python
my_list = [1, 2, 3, "hello", True]
```

#### Indexing et slicing

```python
my_list[0]    # premier élément : 1
my_list[-1]   # dernier élément : True
my_list[1:3]  # sous-liste de l'index 1 à 2 : [2, 3]
my_list[::-1] # liste inversée
```

#### Méthodes principales

| Méthode | Effet |
|---------|-------|
| `append(x)` | Ajouter `x` en fin |
| `insert(i, x)` | Insérer `x` à l'index `i` |
| `remove(x)` | Supprimer la première occurrence de `x` |
| `pop(i)` | Retirer et retourner l'élément à l'index `i` |
| `sort()` | Trier en place |
| `reverse()` | Inverser en place |

---

### Parcourir une liste — 0-print_list_integer.py

```python
def print_list_integer(my_list=[]):
    for i in range(len(my_list)):
        print("{:d}".format(my_list[i]))
```

- `range(len(my_list))` génère les indices de 0 à len-1.
- `"{:d}".format(x)` formate en entier décimal.

---

### Créer une nouvelle liste modifiée — 4-new_in_list.py

En Python, pour ne pas modifier la liste originale, on crée une **copie** :

```python
def new_in_list(my_list, idx, element):
    new = list(my_list)    # copie superficielle
    new[idx] = element
    return new
```

---

### List Comprehensions

Syntaxe compacte pour créer des listes :

```python
# Carrés des nombres pairs de 0 à 9
squares = [x**2 for x in range(10) if x % 2 == 0]
```

**Exemple — 10-divisible_by_2.py :**
```python
def divisible_by_2(my_list=[]):
    return [x % 2 == 0 for x in my_list]
```

---

### Matrices — 6-print_matrix_integer.py

Une matrice en Python est une **liste de listes** :

```python
matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

for row in matrix:
    for j, val in enumerate(row):
        if j < len(row) - 1:
            print("{:d} ".format(val), end="")
        else:
            print("{:d}".format(val))
```

---

### Les tuples

Un **tuple** est une collection ordonnée, **immuable** (non modifiable) :

```python
my_tuple = (1, 2, 3)
# my_tuple[0] = 5  ← TypeError : les tuples ne peuvent pas être modifiés
```

**Cas d'usage :** données qui ne doivent pas changer (coordonnées, retour multiple de fonctions).

#### Tuple unpacking

```python
a, b = (10, 20)        # déballage
a, b = b, a            # échange sans variable temporaire — 12-switch.py
```

---

### Comparer list et tuple

| | List | Tuple |
|--|------|-------|
| Mutable | Oui | Non |
| Syntaxe | `[1, 2, 3]` | `(1, 2, 3)` |
| Performance | Plus lent | Plus rapide |
| Hashable | Non | Oui (si éléments hashables) |
| Usage | Collections variables | Données fixes |

---

## Résumé des fichiers

| Fichier | Concept principal |
|---------|-------------------|
| `0-print_list_integer.py` | Parcours de liste, `range`, `format` |
| `1-element_at.py` | Accès par index, gestion des index invalides |
| `2-replace_in_list.py` | Modification en place |
| `3-print_reversed_list_integer.py` | Inverser une liste |
| `4-new_in_list.py` | Copie de liste, modification sans mutation |
| `5-no_c.py` | Filtrer des caractères d'une chaîne |
| `6-print_matrix_integer.py` | Matrices (listes de listes) |
| `10-divisible_by_2.py` | List comprehension avec condition |
| `11-delete_at.py` | `pop()`, suppression par index |
| `12-switch.py` | Échange de variables, tuple unpacking |
