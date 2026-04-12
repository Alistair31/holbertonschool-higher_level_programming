# Python - RESTful API

## Concepts clés

### Qu'est-ce qu'une API REST ?

Une **API REST** (Representational State Transfer) est une interface web qui suit des conventions pour exposer des ressources via HTTP.

**Principes REST :**
- **Stateless** : chaque requête est indépendante.
- **Ressources identifiées par URLs** : `/users`, `/users/123`.
- **Méthodes HTTP** pour les opérations CRUD.

---

### Méthodes HTTP

| Méthode | Action | Exemple |
|---------|--------|---------|
| `GET` | Lire | `GET /users` → liste des utilisateurs |
| `POST` | Créer | `POST /users` → créer un utilisateur |
| `PUT` | Remplacer | `PUT /users/1` → remplacer l'utilisateur 1 |
| `PATCH` | Modifier | `PATCH /users/1` → modifier partiellement |
| `DELETE` | Supprimer | `DELETE /users/1` → supprimer |

---

### Codes de statut HTTP

| Code | Signification |
|------|---------------|
| `200 OK` | Succès |
| `201 Created` | Ressource créée |
| `400 Bad Request` | Requête invalide |
| `401 Unauthorized` | Non authentifié |
| `403 Forbidden` | Accès interdit |
| `404 Not Found` | Ressource introuvable |
| `500 Internal Server Error` | Erreur serveur |

---

### requests — Consommer une API — task_02_requests.py

```python
import requests

url = "https://jsonplaceholder.typicode.com/posts"
response = requests.get(url)

print(f"Status Code: {response.status_code}")

if response.status_code == 200:
    posts = response.json()   # désérialise le JSON automatiquement
    for post in posts:
        print(post['title'])
```

**Autres méthodes de `requests` :**
```python
requests.get(url)
requests.post(url, json={"key": "value"})
requests.put(url, json=data)
requests.delete(url)
```

---

### Flask — Créer une API REST — task_04_flask.py

```python
from flask import Flask, jsonify, request

app = Flask(__name__)
users = {}   # stockage en mémoire

@app.route("/users/<username>")
def get_user(username):
    if username in users:
        return jsonify(users[username])   # retourne JSON
    return jsonify({"error": "User not found"}), 404

@app.route("/add_user", methods=['POST'])
def add_user():
    data = request.get_json()   # lire le JSON de la requête
    if data is None:
        return jsonify({"error": "Invalid JSON"}), 400
    users[data['username']] = data
    return jsonify({"message": "User added", "user": data}), 201
```

- `jsonify()` : convertit un dict Python en réponse JSON avec les bons headers.
- `request.get_json()` : lit le corps de la requête POST en JSON.
- `methods=['POST']` : restreint la route aux requêtes POST.

---

### HTTP Server simple — task_03_http_server.py

```python
from http.server import HTTPServer, BaseHTTPRequestHandler
import json

class SimpleAPIHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        if self.path == "/":
            self.send_response(200)
            self.send_header("Content-Type", "text/plain")
            self.end_headers()
            self.wfile.write(b"Hello, this is a simple API!")
```

---

### Authentification — task_05_basic_security.py

#### HTTP Basic Auth

```python
from flask_httpauth import HTTPBasicAuth
from werkzeug.security import generate_password_hash, check_password_hash

auth = HTTPBasicAuth()

@auth.verify_password
def verify_password(username, password):
    if username in users and check_password_hash(users[username], password):
        return username

@app.route("/protected")
@auth.login_required   # protéger la route
def protected():
    return f"Hello, {auth.current_user()}!"
```

#### JWT (JSON Web Token)

```python
from flask_jwt_extended import JWTManager, create_access_token, jwt_required

app.config["JWT_SECRET_KEY"] = "secret"
jwt = JWTManager(app)

@app.route("/login", methods=["POST"])
def login():
    token = create_access_token(identity=username)
    return jsonify(access_token=token)

@app.route("/data")
@jwt_required()   # nécessite un JWT valide
def data():
    ...
```

---

## Résumé des fichiers

| Fichier | Concept principal |
|---------|-------------------|
| `task_02_requests.py` | `requests.get()`, `.json()`, codes HTTP |
| `task_03_http_server.py` | Serveur HTTP bas niveau avec `http.server` |
| `task_04_flask.py` | Flask API REST, `jsonify`, `request.get_json()` |
| `task_05_basic_security.py` | HTTP Basic Auth, JWT, `flask_jwt_extended` |
