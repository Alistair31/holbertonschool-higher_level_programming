# JavaScript - DOM Manipulation

## Concepts clés

### Qu'est-ce que le DOM ?

Le **DOM** (Document Object Model) est la représentation en mémoire de la page HTML. JavaScript peut le lire et le modifier pour rendre les pages **interactives**.

```
HTML page
  └── document
       └── html
            ├── head
            └── body
                 ├── header
                 └── main
                      ├── div#content
                      └── ul.my_list
```

---

### Sélectionner des éléments

```javascript
// Par ID (retourne UN élément)
const header = document.getElementById("header");

// Par sélecteur CSS (retourne le PREMIER)
const el = document.querySelector("header");
const el = document.querySelector("#mon-id");
const el = document.querySelector(".ma-classe");

// Par sélecteur CSS (retourne TOUS)
const headers = document.querySelectorAll("header");
```

**Exemple — 0-script.js :**
```javascript
const header = document.querySelectorAll("header");
header[0].style.color = "#FF0000";
```

---

### Modifier le DOM

#### Modifier le style

```javascript
element.style.color = "#FF0000";
element.style.backgroundColor = "blue";
element.style.fontSize = "24px";
```

#### Modifier les classes

```javascript
element.classList.add("my-class");
element.classList.remove("old-class");
element.classList.toggle("active");
element.classList.contains("active");   // true/false
```

#### Modifier le contenu

```javascript
element.textContent = "Nouveau texte";   // texte brut
element.innerHTML = "<b>HTML</b>";        // HTML (attention XSS)
```

#### Modifier les attributs

```javascript
element.setAttribute("href", "https://example.com");
element.getAttribute("href");
element.removeAttribute("style");
```

---

### Créer et supprimer des éléments — 4-script.js

```javascript
const add_item = document.getElementById("add_item");
const my_list = document.querySelector(".my_list");

add_item.addEventListener("click", function() {
    const new_item = document.createElement("li");   // créer un élément
    new_item.textContent = "Item";
    my_list.appendChild(new_item);                   // l'ajouter au DOM
});
```

```javascript
parent.appendChild(child);      // ajouter à la fin
parent.removeChild(child);      // supprimer
parent.insertBefore(new, ref);  // insérer avant un élément
```

---

### Événements — addEventListener

```javascript
element.addEventListener("click", function() {
    // code exécuté au clic
});

element.addEventListener("click", (event) => {
    console.log(event.target);   // l'élément cliqué
});
```

**Événements courants :**

| Événement | Déclencheur |
|-----------|-------------|
| `click` | Clic souris |
| `dblclick` | Double clic |
| `mouseover` | Survol |
| `keydown` | Touche appuyée |
| `submit` | Soumission de formulaire |
| `load` | Page chargée |
| `DOMContentLoaded` | DOM prêt |

---

### Fetch API — Requêtes HTTP asynchrones — 6-script.js

```javascript
fetch("https://api.example.com/data")
    .then(response => response.json())   // convertir la réponse en JSON
    .then(data => {
        document.getElementById("result").textContent = data.name;
    })
    .catch(error => console.error("Erreur:", error));
```

**Syntaxe async/await (plus lisible) :**
```javascript
async function loadData() {
    try {
        const response = await fetch("https://api.example.com/data");
        const data = await response.json();
        document.getElementById("result").textContent = data.name;
    } catch (error) {
        console.error("Erreur:", error);
    }
}
```

---

### Exemple complet — 8-script.js

```javascript
fetch("https://hellosalut.stefanbohacek.com/?lang=fr")
    .then(response => response.json())
    .then(data => {
        const hello = document.getElementById("hello");
        hello.textContent = data.hello;   // affiche "Bonjour" dans l'élément
    });
```

---

### Inclure un script dans le HTML

```html
<!-- Dans le <head> avec defer -->
<script src="1-script.js" defer></script>

<!-- Avant </body> -->
<script src="1-script.js"></script>
```

- `defer` : le script s'exécute après que le DOM soit chargé.

---

## Résumé des fichiers

| Fichier | Concept principal |
|---------|-------------------|
| `0-script.js` | `querySelectorAll`, `style.color` |
| `1-script.js` | `getElementById`, modifier une classe |
| `2-script.js` | `classList.remove`, `classList.add` |
| `3-script.js` | `addEventListener("click")` |
| `4-script.js` | `createElement`, `appendChild` |
| `5-script.js` | Modifier le texte d'un élément |
| `6-script.js` | `fetch()`, `.then()`, API externe |
| `7-script.js` | `fetch()`, liste d'éléments dynamique |
| `8-script.js` | `fetch()` avec paramètre de langue |
