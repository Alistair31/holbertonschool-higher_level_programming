# Python - Serialization

## Concepts clés

### Qu'est-ce que la sérialisation ?

La **sérialisation** convertit un objet Python en un format stockable ou transmissible (fichier, réseau). La **désérialisation** effectue l'opération inverse.

```
Objet Python  →  sérialisation  →  bytes/texte  →  fichier ou réseau
fichier       →  désérialisation →  Objet Python
```

---

### JSON — 0-task_basic_serialization.py

Le format JSON est lisible par l'humain et universel (compatible tous langages).

```python
import json

# Sérialiser et sauvegarder
def serialize_and_save_to_file(data, filename):
    with open(filename, "w") as f:
        json.dump(data, f)

# Charger et désérialiser
def load_and_deserialize(filename):
    with open(filename, "r") as f:
        return json.load(f)
```

**Limites du JSON :** ne peut pas sérialiser des objets Python personnalisés directement (uniquement dict, list, str, int, float, bool, None).

---

### Pickle — task_01_pickle.py

**Pickle** est un format binaire Python-natif qui peut sérialiser **n'importe quel objet Python**.

```python
import pickle

class CustomObject:
    def serialize(self, filename):
        with open(filename, "wb") as f:   # mode binaire "wb"
            pickle.dump(self, f)

    @classmethod
    def deserialize(cls, filename):
        try:
            with open(filename, "rb") as f:  # mode binaire "rb"
                return pickle.load(f)
        except Exception:
            return None
```

**Avantages :**
- Sérialise n'importe quel objet Python (classes, fonctions, etc.)
- Préserve le type exact

**Inconvénients :**
- Non lisible par l'humain
- Non portable (spécifique à Python)
- **Risque de sécurité** : ne pas désérialiser des données non fiables

---

### CSV — task_02_csv.py

Le CSV (Comma-Separated Values) est un format texte pour les données tabulaires.

```python
import csv, json

def convert_csv_to_json(filename):
    with open(filename, "r") as csvfile:
        data = list(csv.DictReader(csvfile))
    # DictReader transforme chaque ligne en dictionnaire

    with open("data.json", "w") as jsonfile:
        json.dump(data, jsonfile)
```

**Lecture CSV :**
```python
with open("data.csv", "r") as f:
    reader = csv.reader(f)        # liste de listes
    reader = csv.DictReader(f)    # liste de dicts (avec header)
```

**Écriture CSV :**
```python
with open("out.csv", "w", newline="") as f:
    writer = csv.writer(f)
    writer.writerow(["name", "age"])   # en-tête
    writer.writerow(["Alice", 30])     # données
```

---

### XML — task_03_xml.py

Le XML est un format structuré, verbeux mais très utilisé.

```python
import xml.etree.ElementTree as ET

# Lire un XML
tree = ET.parse("data.xml")
root = tree.getroot()
for child in root:
    print(child.tag, child.attrib, child.text)

# Écrire un XML
root = ET.Element("data")
child = ET.SubElement(root, "name")
child.text = "Alice"
tree = ET.ElementTree(root)
tree.write("out.xml", encoding="utf-8", xml_declaration=True)
```

---

### Comparaison des formats

| Format | Lisible | Python-only | Types supportés | Usage |
|--------|---------|-------------|-----------------|-------|
| JSON | Oui | Non | Basiques | API REST, config |
| Pickle | Non | Oui | Tous | Cache Python |
| CSV | Oui | Non | Texte tabulaire | Données tabulaires |
| XML | Oui | Non | Texte structuré | Config, SOAP |

---

## Résumé des fichiers

| Fichier | Concept principal |
|---------|-------------------|
| `task_00_basic_serialization.py` | `json.dump` / `json.load` |
| `task_01_pickle.py` | `pickle.dump` / `pickle.load`, mode binaire |
| `task_02_csv.py` | `csv.DictReader`, conversion CSV → JSON |
| `task_03_xml.py` | `xml.etree.ElementTree`, lecture/écriture XML |
