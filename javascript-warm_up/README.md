# JavaScript - Warm Up

## Concepts clés

### JavaScript côté serveur avec Node.js

Ces scripts s'exécutent avec **Node.js** (JavaScript côté serveur) :

```bash
node 0-javascript_is_amazing.js
# ou avec le shebang : #!/usr/bin/node
./0-javascript_is_amazing.js
```

---

### Affichage — console.log

```javascript
console.log("Hello, World!");
console.log('C is fun\nPython is cool\nJavaScript is amazing');
```

- `\n` : saut de ligne (comme en C).
- Guillemets simples ou doubles sont équivalents.

---

### Variables — const, let, var

```javascript
const pi = 3.14;     // constante — ne peut pas être réassignée
let count = 0;       // variable — peut être réassignée
var old = "éviter";  // ancien style — portée de fonction (déconseillé)
```

---

### process.argv — Arguments de la ligne de commande

```javascript
const args = process.argv;
// args[0] = chemin de node
// args[1] = chemin du script
// args[2] = premier argument passé
```

**Exemple — 2-arguments.js :**
```javascript
const args = process.argv;
if (args.length > 3) {
    console.log('Arguments found');
} else if (args.length === 3) {
    console.log('Argument found');
} else {
    console.log('No argument');
}
```

---

### Conversion de types

```javascript
parseInt("42")      // → 42 (entier)
parseFloat("3.14")  // → 3.14 (flottant)
Number("42")        // → 42
String(42)          // → "42"
isNaN("hello")      // → true (Not a Number)
isNaN(42)           // → false
```

**Exemple — 5-to_integer.js :**
```javascript
const n = parseInt(process.argv[2]);
if (isNaN(n)) {
    console.log('Not a number');
} else {
    console.log('My number:', n);
}
```

---

### Conditions

```javascript
if (condition) {
    // ...
} else if (autre) {
    // ...
} else {
    // ...
}
```

**Opérateurs de comparaison :**
- `===` : égalité stricte (type ET valeur) — préférer à `==`
- `!==` : inégalité stricte
- `==` : égalité lâche (conversion de type implicite — éviter)

---

### Boucles

```javascript
// for classique
for (let i = 0; i < 10; i++) {
    console.log(i);
}

// while
let i = 0;
while (i < 10) {
    console.log(i);
    i++;
}
```

---

### Fonctions

```javascript
function add(a, b) {
    return a + b;
}

// Fonction fléchée (arrow function)
const add = (a, b) => a + b;
```

**Exemple — 10-factorial.js (récursion) :**
```javascript
function factorial(num) {
    if (num === 0 || isNaN(num)) {
        return 1;
    }
    return num * factorial(num - 1);
}
console.log(factorial(parseInt(process.argv[2])));
```

---

### Objets

```javascript
const myObject = {
    type: 'object',
    value: 12
};

console.log(myObject);
myObject.value = 89;    // modifier une propriété (même avec const !)
console.log(myObject.value);
```

- `const` empêche la réassignation de la variable, pas la modification de l'objet.
- Accès aux propriétés : `obj.prop` ou `obj["prop"]`.

---

### Différences JavaScript vs Python

| Concept | Python | JavaScript |
|---------|--------|------------|
| Affichage | `print(x)` | `console.log(x)` |
| Arguments | `sys.argv` | `process.argv` |
| Non-défini | `None` | `undefined` / `null` |
| Booléens | `True/False` | `true/false` |
| Chaînes | `f"{x}"` | `` `${x}` `` |
| Type check | `isinstance` | `typeof` |

---

## Résumé des fichiers

| Fichier | Concept principal |
|---------|-------------------|
| `0-javascript_is_amazing.js` | `console.log`, `const` |
| `1-multi_languages.js` | `\n` dans les chaînes |
| `2-arguments.js` | `process.argv`, `length` |
| `3-value_argument.js` | `process.argv[2]` |
| `4-concat.js` | Concaténation de chaînes |
| `5-to_integer.js` | `parseInt`, `isNaN` |
| `10-factorial.js` | Récursion, conversion, `isNaN` |
| `11-second_biggest.js` | Tri de tableau `sort()` |
| `12-object.js` | Objets, modification de propriétés |
| `13-add.js` | Exporter une fonction avec `exports` |
