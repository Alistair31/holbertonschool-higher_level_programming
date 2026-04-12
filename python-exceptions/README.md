# Python - Exceptions

## Concepts clés

### Qu'est-ce qu'une exception ?

Une **exception** est une erreur qui survient pendant l'exécution du programme et interrompt le flux normal. Python permet de les **attraper** et de les gérer sans arrêter le programme.

---

### Structure try / except / else / finally

```python
try:
    # code qui peut lever une exception
    result = 10 / 0
except ZeroDivisionError:
    # code exécuté si ZeroDivisionError est levée
    print("Division par zéro !")
except (TypeError, ValueError) as e:
    # attraper plusieurs types à la fois
    print(f"Erreur : {e}")
else:
    # code exécuté si AUCUNE exception n'a été levée
    print("Succès")
finally:
    # code TOUJOURS exécuté, qu'il y ait eu exception ou non
    print("Fin du bloc")
```

---

### safe_print_list — 0-safe_print_list.py

```python
def safe_print_list(my_list=[], x=0):
    count = 0
    for i in range(x):
        try:
            print("{}".format(my_list[i]), end="")
            count += 1
        except IndexError:
            break   # s'arrêter si l'index dépasse la liste
    print("")
    return count
```

- `IndexError` : levée quand on accède à un index hors limites.
- `break` dans le `except` : sortir de la boucle proprement.

---

### safe_print_integer — 1-safe_print_integer.py

```python
def safe_print_integer(value):
    try:
        print("{:d}".format(value))
        return True
    except (TypeError, ValueError):
        return False
```

- `{:d}` : format entier — lève une `ValueError` si `value` n'est pas un entier.
- Retourne `True` en cas de succès, `False` sinon.

---

### safe_print_division — 3-safe_print_division.py

```python
def safe_print_division(a, b):
    try:
        result = a / b
    except (TypeError, ZeroDivisionError):
        result = None
    finally:
        print("Inside result: {}".format(result))
        return result
```

**`finally`** : s'exécute **toujours**, même si une exception a été levée. Utile pour les nettoyages (fermer un fichier, libérer une ressource).

---

### Lever une exception — 5-raise_exception.py

```python
def raise_exception():
    raise TypeError("my error message")
```

- `raise` lève manuellement une exception.
- On peut lever n'importe quel type d'exception built-in ou personnalisé.

---

### Liste des exceptions courantes

| Exception | Cause typique |
|-----------|---------------|
| `TypeError` | Mauvais type d'argument |
| `ValueError` | Valeur incorrecte (bon type, mauvaise valeur) |
| `IndexError` | Index hors limites d'une liste |
| `KeyError` | Clé absente d'un dictionnaire |
| `ZeroDivisionError` | Division par zéro |
| `AttributeError` | Attribut inexistant sur un objet |
| `NameError` | Variable non définie |
| `FileNotFoundError` | Fichier introuvable |
| `ImportError` | Module introuvable |
| `StopIteration` | Itérateur épuisé |

---

### Exceptions personnalisées

```python
class MyError(Exception):
    pass

raise MyError("mon message personnalisé")
```

---

### Différence erreur vs exception

- **SyntaxError** : détectée avant l'exécution (code mal formé).
- **Exception** : détectée pendant l'exécution.

---

## Résumé des fichiers

| Fichier | Concept principal |
|---------|-------------------|
| `0-safe_print_list.py` | `try/except IndexError`, `break` |
| `1-safe_print_integer.py` | `try/except TypeError/ValueError`, `{:d}` |
| `2-safe_print_list_integers.py` | Filtrage de types dans une liste |
| `3-safe_print_division.py` | `try/except/finally`, division sécurisée |
| `4-list_division.py` | Gestion multiple d'exceptions |
| `5-raise_exception.py` | `raise TypeError` |
| `6-raise_exception_msg.py` | `raise NameError("message")` |
