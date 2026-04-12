# Python - Server-Side Rendering

## Concepts clés

### Qu'est-ce que le Server-Side Rendering (SSR) ?

Le **SSR** génère le HTML **côté serveur** avant de l'envoyer au client. Contrairement au Client-Side Rendering (CSR) où JavaScript génère le HTML dans le navigateur.

**Avantages du SSR :**
- Meilleur SEO (les moteurs de recherche voient le contenu)
- Premier chargement plus rapide
- Fonctionne sans JavaScript côté client

---

### Templates — task_00_intro.py

Avant Flask, on peut générer des fichiers texte avec des templates simples :

```python
def generate_invitations(template, attendees):
    for i, attendee in enumerate(attendees, start=1):
        content = template
        for key in ["name", "event_title", "event_date", "event_location"]:
            value = attendee.get(key, "N/A")
            content = content.replace("{" + key + "}", str(value))
        with open(f"output_{i}.txt", "w") as f:
            f.write(content)
```

- `str.replace(ancien, nouveau)` : substitution simple de texte.
- `dict.get(key, "N/A")` : retourne `"N/A"` si la clé est absente.

---

### Flask — Framework Web Python — task_01_jinja.py

```python
from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/about')
def about():
    return render_template('about.html')

if __name__ == '__main__':
    app.run(debug=True, port=5000)
```

- `Flask(__name__)` : crée l'application Flask.
- `@app.route('/')` : décorateur qui associe une URL à une fonction.
- `render_template('index.html')` : charge et retourne le fichier HTML depuis `templates/`.

---

### Jinja2 — Moteur de templates

Jinja2 est le moteur de templates intégré à Flask. Il permet d'insérer des données Python dans le HTML.

#### Syntaxe Jinja2

```html
<!-- Variables -->
<h1>{{ title }}</h1>
<p>{{ user.name }}</p>

<!-- Conditions -->
{% if user %}
    <p>Bienvenue {{ user.name }}</p>
{% else %}
    <p>Bienvenue, inconnu</p>
{% endif %}

<!-- Boucles -->
{% for item in items %}
    <li>{{ item }}</li>
{% endfor %}

<!-- Héritage de templates -->
{% extends "base.html" %}
{% block content %}
    <p>Contenu spécifique à cette page</p>
{% endblock %}
```

---

### Passer des données au template — task_02_logic.py

```python
@app.route('/items')
def items():
    items = ["apple", "banana", "cherry"]
    return render_template('items.html', items=items)
```

```html
<!-- items.html -->
<ul>
{% for item in items %}
    <li>{{ item }}</li>
{% endfor %}
</ul>
```

---

### Lire depuis des fichiers — task_03_files.py

```python
import json

@app.route('/products')
def products():
    with open('products.json', 'r') as f:
        products = json.load(f)
    return render_template('products.html', products=products)
```

---

### SQLite avec Flask — task_04_db.py

```python
import sqlite3

@app.route('/products')
def products():
    conn = sqlite3.connect('products.db')
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM Products")
    products = cursor.fetchall()
    conn.close()
    return render_template('product_display.html', products=products)
```

---

### Structure d'un projet Flask

```
project/
├── app.py             # fichier principal
├── templates/         # fichiers HTML Jinja2
│   ├── base.html      # template de base
│   ├── index.html
│   └── about.html
└── static/            # CSS, JS, images
    └── style.css
```

---

## Résumé des fichiers

| Fichier | Concept principal |
|---------|-------------------|
| `task_00_intro.py` | Templates texte, `str.replace()`, génération de fichiers |
| `task_01_jinja.py` | Flask, `@app.route`, `render_template` |
| `task_02_logic.py` | Passer des variables aux templates Jinja2 |
| `task_03_files.py` | Lire JSON/CSV et afficher avec Jinja2 |
| `task_04_db.py` | SQLite avec Flask, requêtes SQL dynamiques |
