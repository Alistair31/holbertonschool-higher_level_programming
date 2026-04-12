# Python - More Data Structures: Set, Dictionary

## Concepts clés

### Les ensembles (set)

Un **set** est une collection **non ordonnée** d'éléments **uniques** et **hashables**.

```python
my_set = {1, 2, 3, 3, 2}
print(my_set)   # {1, 2, 3} — les doublons sont supprimés

empty_set = set()   # set vide (pas {} qui crée un dict vide)
```

#### Opérations sur les sets

| Opération | Syntaxe | Signification |
|-----------|---------|---------------|
| Union | `s1 \| s2` | Tous les éléments |
| Intersection | `s1 & s2` | Éléments communs |
| Différence | `s1 - s2` | Dans s1 mais pas s2 |
| Diff. symétrique | `s1 ^ s2` | Dans l'un ou l'autre, pas les deux |

**Exemple — common_elements (3-common_elements.py) :**
```python
def common_elements(set_1, set_2):
    return (set_1 & set_2)   # intersection
```

**Exemple — only_diff_elements (4-only_diff_elements.py) :**
```python
def only_diff_elements(set_1, set_2):
    return (set_1 ^ set_2)   # différence symétrique
```

---

### Les dictionnaires (dict)

Un **dictionnaire** associe des **clés** à des **valeurs**. Les clés doivent être hashables (uniques).

```python
my_dict = {"name": "Alice", "age": 30}
print(my_dict["name"])   # "Alice"

my_dict["city"] = "Paris"   # ajouter une clé
del my_dict["age"]           # supprimer une clé
```

#### Méthodes principales

| Méthode | Retourne |
|---------|----------|
| `d.keys()` | Vue des clés |
| `d.values()` | Vue des valeurs |
| `d.items()` | Vue des paires (clé, valeur) |
| `d.get(key, default)` | Valeur ou default si clé absente |
| `d.update({...})` | Fusionner un autre dict |

---

### uniq_add — 2-uniq_add.py

```python
def uniq_add(my_list=[]):
    return sum(set(my_list))   # somme sans doublons
```

- `set(my_list)` : convertit la liste en set → supprime les doublons.

---

### Itérer sur un dictionnaire

```python
# Itérer sur les clés
for key in my_dict:
    print(key)

# Itérer sur les paires
for key, value in my_dict.items():
    print(f"{key}: {value}")
```

---

### best_score — 10-best_score.py

```python
def best_score(a_dictionary):
    if not a_dictionary:
        return None
    return max(a_dictionary, key=a_dictionary.get)
```

- `max(..., key=fn)` : retourne l'élément qui maximise `fn(element)`.
- `a_dictionary.get` : `max` applique `.get(key)` à chaque clé pour comparer les valeurs.

---

### map() et lambda — 11-multiply_list_map.py

```python
def multiply_list_map(my_list=[], number=0):
    return list(map(lambda x: x * number, my_list))
```

- `map(fn, iterable)` : applique `fn` à chaque élément de `iterable`.
- `lambda x: x * number` : fonction anonyme (sans nom).
- `list(...)` : convertit le résultat `map` en liste.

**Équivalent avec list comprehension :**
```python
[x * number for x in my_list]
```

---

### roman_to_int — 12-roman_to_int.py

```python
def roman_to_int(roman_string):
    if not isinstance(roman_string, str):
        return 0
    values = {'I': 1, 'V': 5, 'X': 10, 'L': 50,
              'C': 100, 'D': 500, 'M': 1000}
    result = 0
    prev = 0
    for char in reversed(roman_string):
        curr = values.get(char, 0)
        if curr < prev:
            result -= curr   # soustraction (ex: IV = 5 - 1)
        else:
            result += curr
        prev = curr
    return result
```

---

### Comparaison set vs list vs dict

| | list | set | dict |
|--|------|-----|------|
| Ordonné | Oui | Non | Oui (Python 3.7+) |
| Doublons | Oui | Non | Clés uniques |
| Accès par index | Oui | Non | Par clé |
| Recherche | O(n) | O(1) | O(1) |
| Mutable | Oui | Oui | Oui |

---

## Résumé des fichiers

| Fichier | Concept principal |
|---------|-------------------|
| `0-square_matrix_simple.py` | Matrices (liste de listes), `map` |
| `1-search_replace.py` | Remplacer dans une liste |
| `2-uniq_add.py` | `set()` pour dédoublonner |
| `3-common_elements.py` | Intersection de sets `&` |
| `4-only_diff_elements.py` | Différence symétrique `^` |
| `5-number_keys.py` | `len(dict)` |
| `6-print_sorted_dictionary.py` | `sorted()` sur les clés |
| `7-update_dictionary.py` | Mise à jour d'un dict |
| `8-simple_delete.py` | `pop()` sur un dict |
| `9-multiply_by_2.py` | Créer un nouveau dict avec valeurs modifiées |
| `10-best_score.py` | `max()` avec `key=` |
| `11-multiply_list_map.py` | `map()`, `lambda` |
| `12-roman_to_int.py` | Dict de correspondances, logique romaine |
