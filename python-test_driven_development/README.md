# Python - Test-Driven Development (TDD)

## Concepts clés

### Qu'est-ce que le TDD ?

Le **Test-Driven Development** est une méthodologie de développement où on **écrit les tests avant le code** :

```
1. Écrire un test qui échoue (RED)
2. Écrire le minimum de code pour le faire passer (GREEN)
3. Refactoriser (REFACTOR)
→ Répéter
```

---

### Doctests — tests dans la docstring

Python permet d'écrire des tests directement dans les docstrings via le module `doctest`.

**Format :**
```python
def add_integer(a, b=98):
    """
    Adds two integers.

    >>> add_integer(1, 2)
    3
    >>> add_integer(100, -2)
    98
    >>> add_integer(4, "School")
    Traceback (most recent call last):
    TypeError: b must be an integer
    """
    ...
```

- `>>> expression` : appel à tester.
- Ligne suivante : résultat attendu.
- `Traceback (most recent call last):` suivi du type d'exception : test d'erreur.

**Exécuter les doctests :**
```bash
python3 -m doctest -v tests/0-add_integer.txt
```

---

### Fichiers de tests .txt

On peut aussi écrire les tests dans des fichiers séparés :

```
# tests/0-add_integer.txt
>>> add_integer = __import__('0-add_integer').add_integer

>>> add_integer(1, 2)
3

>>> add_integer(4, "School")
Traceback (most recent call last):
TypeError: b must be an integer
```

---

### unittest — Tests formels

Le module `unittest` permet des tests plus structurés :

```python
import unittest
from 6-max_integer import max_integer

class TestMaxInteger(unittest.TestCase):
    def test_ordered_list(self):
        self.assertEqual(max_integer([1, 2, 3, 4]), 4)

    def test_empty_list(self):
        self.assertIsNone(max_integer([]))

    def test_negative_numbers(self):
        self.assertEqual(max_integer([-5, -1, -3]), -1)

if __name__ == '__main__':
    unittest.main()
```

**Méthodes d'assertion courantes :**

| Méthode | Test |
|---------|------|
| `assertEqual(a, b)` | `a == b` |
| `assertNotEqual(a, b)` | `a != b` |
| `assertTrue(x)` | `bool(x)` est True |
| `assertFalse(x)` | `bool(x)` est False |
| `assertIsNone(x)` | `x is None` |
| `assertIsNotNone(x)` | `x is not None` |
| `assertRaises(exc, fn, *args)` | `fn(*args)` lève `exc` |
| `assertIn(a, b)` | `a in b` |

---

### add_integer — 0-add_integer.py

```python
def add_integer(a, b=98):
    if isinstance(a, (int, float)) is False:
        raise TypeError("a must be an integer")
    if isinstance(b, (int, float)) is False:
        raise TypeError("b must be an integer")
    return int(a) + int(b)   # convertir float en int avant addition
```

---

### Cas limites à tester

Bonnes pratiques TDD — toujours tester :
- **Cas nominal** : entrée correcte attendue.
- **Cas limites** : valeurs extrêmes (0, négatifs, très grands nombres).
- **Cas d'erreur** : mauvais types, valeurs invalides.
- **Cas vides** : liste vide, chaîne vide, None.

---

### Pourquoi le TDD ?

- Force à réfléchir à l'interface avant l'implémentation.
- Documenter le comportement attendu de la fonction.
- Régression : détecter les bugs introduits par de nouvelles modifications.
- Confiance pour refactoriser.

---

## Résumé des fichiers

| Fichier | Concept principal |
|---------|-------------------|
| `0-add_integer.py` | Validation de types, `int()` float conversion |
| `2-matrix_divided.py` | Validation de matrice, division |
| `3-say_my_name.py` | Validation de types, f-strings |
| `4-print_square.py` | Validation entier positif |
| `5-text_indentation.py` | Manipulation de chaînes, caractères spéciaux |
| `6-max_integer.py` | Algorithme, liste vide |
| `tests/` | Fichiers doctest `.txt` pour chaque module |
