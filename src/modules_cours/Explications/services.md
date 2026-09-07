# Module `services.py`

## 🎯 Rôle du module

Le module **`services.py`** regroupe les fonctions qui réalisent les **opérations sur les groupes de participants**.

Il constitue une couche intermédiaire entre :

* les **données** définies dans `data.py` ;
* les fonctions de **lecture des saisies** définies dans `reader.py` ;
* le **programme principal**, qui utilise les services proposés.

L'objectif est de ne pas placer toutes les opérations dans le programme principal et de **regrouper les fonctionnalités liées aux groupes dans un module dédié**.

---

## 🏗️ Position du module dans l'application

```text
                 APPLICATION
                      │
          ┌───────────┼───────────┐
          │           │           │
          ▼           ▼           ▼
       data.py    services.py   reader.py
          │           │           │
          │           │           │
       Données     Services      Saisie
          │           │           │
          │      ┌────┼────┐      │
          │      │    │    │      │
          │      ▼    ▼    ▼      │
          │    créer valider      │
          │          afficher     │
          │          sélectionner │
          │           │           │
          └───────────┼───────────┘
                      ▼
             programme principal
```

### Principe

```text
data.py
   ↓
fournit les données

services.py
   ↓
travaille avec les données

reader.py
   ↓
gère les saisies

programme principal
   ↓
coordonne l'ensemble
```

---

# 📦 Dépendances

Le module utilise deux ressources externes.

## `data.py`

```python
from data import groupes
```

Le module récupère la liste des groupes définie dans `data.py`.

Par exemple :

```python
groupes = [
    "python",
    "java",
    "web"
]
```

## `reader.py`

```python
from reader import read_integer_min_max
```

La fonction `read_integer_min_max()` permet de récupérer un nombre saisi par l'utilisateur tout en contrôlant ses limites.

---

# 🔧 Fonctions disponibles

Le module fournit quatre fonctions principales :

| Fonction            | Responsabilité                                            |
| ------------------- | --------------------------------------------------------- |
| `groupe_set()`      | Transformer la liste des groupes en dictionnaire numéroté |
| `is_items_str()`    | Vérifier le type des valeurs d'un dictionnaire            |
| `display_groupes()` | Afficher les groupes                                      |
| `select_group()`    | Afficher les groupes et permettre leur sélection          |

---

# 1️⃣ `groupe_set()`

## Description

La fonction `groupe_set()` transforme la liste `groupes` en un dictionnaire dont les clés correspondent aux numéros des groupes.

### Exemple

Liste initiale :

```python
groupes = [
    "python",
    "java",
    "web"
]
```

Résultat :

```python
{
    "1": "python",
    "2": "java",
    "3": "web"
}
```

### Fonctionnement

```python
def groupe_set():
    dico_groupes = {}

    for pointer in range(0, len(groupes)):
        key = str(pointer + 1)
        dico_groupes[key] = groupes[pointer]

    return dico_groupes
```

### Responsabilité

> Transformer les données afin de les rendre facilement utilisables pour l'affichage et la sélection.

---

# 2️⃣ `is_items_str()`

## Description

La fonction `is_items_str()` vérifie que le paramètre reçu est un dictionnaire et que **toutes ses valeurs sont de type `str`**.

### Exemple valide

```python
groupes = {
    "1": "python",
    "2": "java",
    "3": "web"
}
```

Résultat :

```python
True
```

### Exemple invalide

```python
groupes = {
    "1": "python",
    "2": 123,
    "3": "web"
}
```

Résultat :

```python
False
```

### Fonctionnement

```python
def is_items_str(dico_groups):

    if not isinstance(dico_groups, dict):
        raise TypeError(
            "le paramètre doit-être un dictionnaire valide."
        )

    for key in dico_groups:
        if not isinstance(dico_groups[key], str):
            return False

    return True
```

### Responsabilité

> Vérifier la validité du contenu du dictionnaire.

Cette fonction est une fonction de **validation**.

---

# 3️⃣ `display_groupes()`

## Description

La fonction `display_groupes()` affiche les différents groupes dans la console.

Elle vérifie auparavant que le dictionnaire reçu est valide.

### Exemple

Pour :

```python
{
    "1": "python",
    "2": "java",
    "3": "web"
}
```

l'affichage sera :

```text
1 - Python
2 - Java
3 - Web
```

### Fonctionnement

```python
def display_groupes(dico_groups):

    if not isinstance(dico_groups, dict):
        raise TypeError(
            "le paramètre doit-être un dictionnaire valide."
        )

    if not is_items_str(dico_groups):
        raise TypeError(
            "Le dictionnaire n'est pas valide, "
            "il faut que les items soit des str."
        )

    for key, value in dico_groups.items():
        print(f" {key} - {value.capitalize()}")
```

### Responsabilité

> Présenter les groupes à l'utilisateur.

Cette fonction montre également le principe de **réutilisation d'une fonction** :

```text
display_groupes()
       │
       ▼
is_items_str()
       │
       ▼
validation
```

---

# 4️⃣ `select_group()`

## Description

La fonction `select_group()` permet à l'utilisateur de **sélectionner un groupe**.

Elle réalise plusieurs opérations :

1. validation du message ;
2. validation du dictionnaire ;
3. création d'un message par défaut ;
4. affichage du message ;
5. affichage des groupes ;
6. lecture du choix de l'utilisateur ;
7. contrôle de la valeur saisie.

### Exemple

```python
dico_groupes = groupe_set()

groupe = select_group(
    "Sélectionner un groupe",
    dico_groupes
)
```

Affichage :

```text
Sélectionner un groupe:

1 - Python
2 - Java
3 - Web

Votre choix de groupe :
```

La fonction retourne ensuite le numéro choisi.

---

# 🔗 Réutilisation des fonctions

Une caractéristique importante de ce module est que les fonctions peuvent **collaborer entre elles**.

```text
select_group()
      │
      ├── vérifie le dictionnaire
      │
      ├── appelle is_items_str()
      │
      ├── appelle display_groupes()
      │
      └── appelle read_integer_min_max()
```

On évite ainsi de recopier plusieurs fois le même code.

---

# 🧩 Principe de responsabilité

Le module illustre le principe :

> **Une fonction doit avoir une responsabilité clairement identifiée.**

Par exemple :

```text
groupe_set()
     ↓
transformer les données

is_items_str()
     ↓
valider les données

display_groupes()
     ↓
afficher les données

select_group()
     ↓
permettre la sélection
```

Cette organisation rend le programme :

* plus lisible ;
* plus facile à tester ;
* plus facile à maintenir ;
* plus facile à faire évoluer ;
* plus facilement réutilisable.

---

# ⚠️ Point d'attention

Dans la fonction `select_group()`, le code actuel contient :

```python
len(dico_group) + 1
```

Si le dictionnaire contient 3 groupes, cela peut autoriser la valeur `4`.

La limite maximale devrait normalement être :

```python
len(dico_group)
```

soit :

```python
return read_integer_min_max(
    "Votre choix de groupe : ",
    1,
    len(dico_group)
)
```

Ainsi, avec trois groupes, seules les valeurs suivantes sont acceptées :

```text
1
2
3
```

---

# 🎓 Intérêt pédagogique

Le module `services.py` permet d'introduire plusieurs notions fondamentales de Python.

### Fonctions

Chaque fonctionnalité est isolée dans une fonction :

```python
def groupe_set():
def is_items_str():
def display_groupes():
def select_group():
```

### Paramètres

Les fonctions peuvent recevoir des données :

```python
display_groupes(dico_groups)
```

### Valeur de retour

Une fonction peut retourner un résultat :

```python
return dico_groupes
```

ou :

```python
return read_integer_min_max(...)
```

### Validation

Les paramètres peuvent être contrôlés avec :

```python
isinstance()
```

et :

```python
raise TypeError
```

### Réutilisation

Une fonction peut appeler une autre fonction :

```python
display_groupes()
       ↓
is_items_str()
```

### Modularité

Les fonctionnalités sont réparties dans plusieurs fichiers :

```text
data.py
   → données

reader.py
   → saisies

services.py
   → opérations sur les groupes

menu.py
   → affichage des menus

main.py
   → orchestration de l'application
```

---

# 🚀 Exemple d'utilisation

```python
from services import groupe_set, display_groupes, select_group

# Création du dictionnaire des groupes
dico_groupes = groupe_set()

# Affichage
display_groupes(dico_groupes)

# Sélection
choix = select_group(
    "Choisir un groupe",
    dico_groupes
)

print(f"Groupe choisi : {choix}")
```

---

# 📌 Synthèse

Le module `services.py` constitue une **couche de services** de l'application.

Il ne contient pas directement les données et ne constitue pas le programme principal.

Son rôle est de fournir des fonctions permettant de :

```text
┌──────────────────────────────┐
│          services.py         │
├──────────────────────────────┤
│                              │
│  Transformer les données     │
│          ↓                   │
│  Valider les données         │
│          ↓                   │
│  Afficher les groupes        │
│          ↓                   │
│  Sélectionner un groupe      │
│                              │
└──────────────────────────────┘
```

Cette organisation constitue une première étape vers une **application Python modulaire**, où chaque module possède une responsabilité clairement définie.

> **Données → Services → Interface → Programme principal**

C'est cette séparation des responsabilités qui constitue l'un des objectifs essentiels du **refactoring**.
