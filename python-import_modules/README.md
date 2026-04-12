# Python - Import & Modules

## Concepts clés

### Importer des modules

Un **module** est un fichier `.py` réutilisable contenant des fonctions, classes ou variables.

```python
import math             # importer le module entier
from math import sqrt   # importer une fonction spécifique
from math import *      # importer tout (déconseillé)
import math as m        # alias
```

---

### Importer depuis un fichier local — 0-add.py

```python
if __name__ == "__main__":
    from add_0 import add   # importer la fonction add depuis add_0.py
    a = 1
    b = 2
    print("{} + {} = {}".format(a, b, add(a, b)))
```

- `from add_0 import add` : importe uniquement la fonction `add` du fichier `add_0.py`.
- Python cherche d'abord dans le répertoire courant, puis dans le `PYTHONPATH`, puis dans la bibliothèque standard.

---

### `if __name__ == "__main__"`

Ce bloc est exécuté **seulement** quand le fichier est lancé directement, pas quand il est importé en tant que module.

```python
# module_a.py
def ma_fonction():
    return 42

if __name__ == "__main__":
    print(ma_fonction())   # exécuté seulement si : python3 module_a.py
```

Si on fait `import module_a`, la ligne `print(...)` ne sera **pas** exécutée.

---

### sys.argv — Arguments de la ligne de commande — 2-args.py

```python
from sys import argv

# argv[0] = nom du script
# argv[1], argv[2], ... = arguments passés au script
```

**Exemple :**
```bash
python3 2-args.py Holberton School
# argv = ['2-args.py', 'Holberton', 'School']
# len(argv) = 3
```

```python
from sys import argv

if len(argv) == 1:
    print("0 arguments.")
else:
    print(f"{len(argv) - 1} arguments:")
    for i in range(1, len(argv)):
        print(f"{i}: {argv[i]}")
```

---

### Les modules de la bibliothèque standard

Quelques modules couramment utilisés :

| Module | Usage |
|--------|-------|
| `sys` | Système, argv, stdin/stdout/stderr |
| `os` | Système de fichiers, variables d'environnement |
| `math` | Fonctions mathématiques (`sqrt`, `pi`, etc.) |
| `random` | Génération de nombres aléatoires |
| `json` | Sérialisation JSON |
| `datetime` | Dates et heures |
| `re` | Expressions régulières |

---

### Modules personnalisés — structure

```python
# calculator_1.py
def add(a, b):
    return a + b

def sub(a, b):
    return a - b
```

```python
# 1-calculation.py
from calculator_1 import add, sub

print(add(10, 5))
print(sub(10, 5))
```

---

### Infinite add — 3-infinite_add.py

```python
from sys import argv

result = 0
for i in range(1, len(argv)):
    result += int(argv[i])
print(result)
```

Additionne tous les arguments numériques passés en ligne de commande.

---

## Résumé des fichiers

| Fichier | Concept principal |
|---------|-------------------|
| `0-add.py` | `import depuis fichier local`, `__name__ == "__main__"` |
| `1-calculation.py` | Importer plusieurs fonctions |
| `2-args.py` | `sys.argv`, arguments ligne de commande |
| `3-infinite_add.py` | Boucle sur `argv`, `int()` conversion |
| `5-variable_load.py` | Importer une variable depuis un module |
