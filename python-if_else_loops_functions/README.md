# Python - if/else, Loops, Functions

## Concepts clés

### If / elif / else

```python
number = random.randint(-10, 10)

if number > 0:
    print(f"{number} is positive")
elif number < 0:
    print(f"{number} is negative")
else:
    print(f"{number} is zero")
```

- `elif` : contraction de "else if".
- En Python, l'**indentation** délimite les blocs (pas d'accolades).
- `random.randint(a, b)` retourne un entier aléatoire entre `a` et `b` inclus.

---

### La boucle for

```python
for variable in iterable:
    # corps
```

**Exemples :**

```python
for i in range(10):        # 0 à 9
    print(i)

for letter in "abc":       # itérer sur une chaîne
    print(letter)

for i in range(1, 26):     # 1 à 25
    print(chr(i + 96))     # affiche a à z
```

- `range(n)` : de 0 à n-1
- `range(a, b)` : de a à b-1
- `range(a, b, step)` : de a à b avec pas de `step`

---

### La boucle while

```python
i = 0
while i < 10:
    print(i)
    i += 1
```

---

### FizzBuzz — 12-fizzbuzz.py

```python
def fizzbuzz():
    for number in range(1, 101):
        if number % 5 == 0 and number % 3 == 0:
            print("FizzBuzz ", end="")
        elif number % 5 == 0:
            print("Buzz ", end="")
        elif number % 3 == 0:
            print("Fizz ", end="")
        else:
            print(f"{number} ", end="")
```

- `end=""` : `print` sans saut de ligne à la fin.
- Tester **d'abord** le cas `% 3 == 0 and % 5 == 0` avant les cas individuels.

---

### Fonctions

```python
def nom_fonction(param1, param2=valeur_defaut):
    """Docstring : décrit la fonction."""
    # corps
    return resultat
```

**Exemple — 10-add.py :**
```python
def add(a, b):
    return a + b
```

**Exemple — 11-pow.py :**
```python
def pow(a, b):
    return a ** b
```

---

### chr() et ord() — manipulation de caractères

```python
chr(97)   # → 'a'  (code ASCII → caractère)
ord('a')  # → 97   (caractère → code ASCII)
```

**Afficher l'alphabet :**
```python
for i in range(26):
    print(chr(ord('a') + i), end="")
```

---

### last_digit — 1-last_digit.py

```python
number = random.randint(-10000, 10000)
last_digit = abs(number) % 10   # ou number % 10 en Python (toujours positif)

if last_digit > 5:
    print(f"... and is greater than 5")
elif last_digit == 0:
    print(f"... and is 0")
else:
    print(f"... and is less than 6 and not 0")
```

**Note Python vs C :** En Python, le résultat de `%` a toujours le signe du **diviseur** (pas du dividende) : `-13 % 10 == 7` en Python.

---

### f-strings (formatted string literals)

```python
name = "Alice"
age = 30
print(f"My name is {name} and I am {age} years old.")
# → "My name is Alice and I am 30 years old."
```

- Plus lisibles que `.format()`.
- Peuvent contenir n'importe quelle expression Python : `f"{2 + 2}"` → `"4"`.

---

## Résumé des fichiers

| Fichier | Concept principal |
|---------|-------------------|
| `0-positive_or_negative.py` | if/elif/else, `random.randint` |
| `1-last_digit.py` | Modulo, conditions, f-strings |
| `2-print_alphabet.py` | Boucle `for`, `chr()`, `print(end="")` |
| `3-print_alphabt.py` | Boucle avec exclusion (if dans for) |
| `4-print_hexa.py` | Décimal et hexadécimal `0x{:x}` |
| `5-print_comb2.py` | Boucles imbriquées, combinaisons |
| `6-print_comb3.py` | Boucles imbriquées à 2 chiffres |
| `10-add.py` | Fonction simple, retour de valeur |
| `11-pow.py` | Opérateur puissance `**` |
| `12-fizzbuzz.py` | FizzBuzz, modulo, conditions multiples |
