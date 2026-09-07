Voici un `README.md` complet, dans le même esprit pédagogique que celui de `data_menu.py`, afin de construire progressivement la démarche **refactoring → fonctions → modularité**.

# 📊 `data.py` — Centraliser les données de l'application

## 🎯 Objectif

Le module `data.py` a une responsabilité clairement définie :

> **Initialiser et centraliser les données utilisées par l'application.**

Dans notre application de **gestion des participants**, les données sont organisées sous la forme de trois ensembles Python (`set`) représentant les participants des différents groupes de formation :

```text
data.py
  │
  ├── python
  │
  ├── java
  │
  └── web
```

L'objectif du refactoring est de **séparer les données du reste de l'application**.

On cherche progressivement à obtenir une architecture dans laquelle :

```text
DONNÉES
   ↓
data.py

MENUS
   ↓
data_menu.py

AFFICHAGE
   ↓
affichage.py

LOGIQUE MÉTIER
   ↓
fonctions de gestion

ORCHESTRATION
   ↓
main.py
```

---

# 🧩 1. Le rôle général de `data.py`

Le module `data.py` est responsable de l'**initialisation des données**.

Dans notre application, il contient trois ensembles :

| Ensemble | Contenu                       |
| -------- | ----------------------------- |
| `python` | Participants du groupe Python |
| `java`   | Participants du groupe Java   |
| `web`    | Participants du groupe Web    |

Par exemple :

```python
python = {
    "Alice",
    "Bob",
    "Charlie",
    "David",
    "Emma"
}

java = {
    "Bob",
    "David",
    "Franck",
    "Emma"
}

web = {
    "Alice",
    "Charlie",
    "Franck"
}
```

Ces ensembles constituent les **données initiales** de l'application.

---

# 📦 2. Pourquoi utiliser des ensembles ?

Les participants sont stockés dans des objets de type `set`.

Un ensemble présente plusieurs caractéristiques intéressantes pour cette application :

* les éléments sont uniques ;
* un participant ne peut pas apparaître deux fois dans le même ensemble ;
* les opérations mathématiques sur les ensembles sont directement disponibles ;
* les opérations `union`, `intersection`, `difference`, etc. sont particulièrement adaptées à notre projet.

Par exemple :

```python
python & web
```

permet d'obtenir les participants communs aux groupes Python et Web.

De même :

```python
python | java
```

permet d'obtenir l'ensemble des participants appartenant au groupe Python ou au groupe Java.

Le choix du `set` est donc directement lié aux fonctionnalités que nous souhaitons développer.

---

# 🏗️ 3. Avant le refactoring

Avant de commencer la modularisation, les données pouvaient être directement déclarées dans le programme principal :

```python
python = {...}
java = {...}
web = {...}
```

Le fichier `main.py` pouvait alors contenir simultanément :

```text
┌──────────────────────────────┐
│           main.py            │
├──────────────────────────────┤
│ Données                      │
│ Menus                        │
│ Affichage                    │
│ Saisies utilisateur          │
│ Gestion des participants     │
│ Recherches                   │
│ Statistiques                 │
│ Traitements                  │
└──────────────────────────────┘
```

Le programme fonctionne, mais plusieurs responsabilités sont regroupées dans le même fichier.

Cela rend le code progressivement :

* plus difficile à lire ;
* plus difficile à modifier ;
* plus difficile à tester ;
* plus difficile à réutiliser.

---

# 🔄 4. Après le refactoring

Avec la création de `data.py`, les données sont déplacées dans un module spécialisé :

```text
                  APPLICATION
                       │
                       ▼
                 ┌──────────┐
                 │ data.py  │
                 └────┬─────┘
                      │
          ┌───────────┼───────────┐
          ▼           ▼           ▼
       python       java         web
```

Les autres modules n'ont plus besoin de connaître la manière dont les données sont initialisées.

Ils peuvent simplement les importer.

---

# 📥 5. Importer les données

Un autre module peut récupérer les ensembles avec :

```python
from data import python, java, web
```

Il peut ensuite les utiliser directement :

```python
print(python)
print(java)
print(web)
```

Ou effectuer des opérations :

```python
communs = python & java
```

Cette séparation permet au module utilisateur de se concentrer sur son propre rôle.

---

# 🎯 6. Une responsabilité unique

Le principe de modularité est de donner à chaque module une **responsabilité clairement identifiée**.

La responsabilité de `data.py` est :

> **Initialiser, centraliser et fournir les données de l'application.**

Son rôle n'est donc pas :

```text
❌ afficher les participants
❌ afficher les menus
❌ demander une saisie
❌ gérer les choix utilisateur
❌ calculer les statistiques
❌ gérer la navigation dans l'application
```

Son rôle est uniquement de :

```text
✅ initialiser les données
✅ centraliser les ensembles
✅ rendre les données disponibles aux autres modules
```

---

# 🧱 7. Séparer données et traitements

Cette séparation est fondamentale dans une démarche de refactoring.

On distingue maintenant :

```text
                 DONNÉES
                    │
                    ▼
                data.py
                    │
                    │ fournit
                    ▼
               les ensembles
                    │
          ┌─────────┴─────────┐
          ▼                   ▼
       Fonctions          Statistiques
       de gestion
```

Les données ne contiennent pas les traitements.

Par exemple, `data.py` ne doit pas contenir une fonction telle que :

```python
def afficher_participants():
    ...
```

Cette fonction appartient à un autre module.

De la même manière, une fonction calculant le nombre de participants appartient à la partie **logique/statistiques** de l'application.

---

# 🔧 8. Modifier les données initiales

Un des avantages immédiats de cette organisation est la facilité de maintenance.

Si l'on souhaite modifier les participants initiaux, il suffit d'intervenir dans :

```text
data.py
```

Par exemple :

```python
python = {
    "Alice",
    "Bob",
    "Charlie",
    "David",
    "Emma",
    "Sophie"
}
```

Les autres modules continuent à utiliser :

```python
from data import python
```

sans avoir besoin de modifier leur code.

---

# 🧠 9. Une seule source pour les données

`data.py` devient ainsi la **source centralisée des données initiales**.

```text
                  data.py
                     │
          ┌──────────┼──────────┐
          │          │          │
          ▼          ▼          ▼
       python      java        web
          │          │          │
          └──────────┼──────────┘
                     │
                     ▼
              autres modules
```

Cela évite de recopier les mêmes données dans plusieurs fichiers.

On évite ainsi une situation comme :

```python
# module1.py
python = {...}

# module2.py
python = {...}

# module3.py
python = {...}
```

Une modification devrait sinon être effectuée à plusieurs endroits.

Avec `data.py`, les données sont définies **une seule fois**.

---

# 🔗 10. `data.py` et `data_menu.py`

Il est important de distinguer les deux modules.

### `data.py`

Contient les **données métier** :

```text
python
java
web
```

### `data_menu.py`

Contient les **données nécessaires aux menus** :

```text
main_title
main_items
main_menu

sub_title
sub_items
sub_menu
```

On obtient donc :

```text
                APPLICATION
                     │
          ┌──────────┴──────────┐
          │                     │
          ▼                     ▼
       data.py            data_menu.py
          │                     │
          ▼                     ▼
 données participants      données menus
```

Cette distinction est importante :

> **Les données des participants ne sont pas les données des menus.**

Chaque module possède sa propre responsabilité.

---

# 🏛️ 11. Vers une architecture modulaire

Après plusieurs étapes de refactoring, l'application peut progressivement prendre cette forme :

```text
                    ┌──────────────┐
                    │    main.py   │
                    │              │
                    │ orchestration│
                    └──────┬───────┘
                           │
        ┌──────────────────┼──────────────────┐
        │                  │                  │
        ▼                  ▼                  ▼
 ┌────────────┐    ┌───────────────┐   ┌───────────────┐
 │  data.py   │    │ data_menu.py  │   │ affichage.py  │
 │            │    │               │   │               │
 │ participants│   │ menus         │   │ afficher_menu │
 └────────────┘    └───────────────┘   └───────────────┘
        │
        ▼
 ┌──────────────────────┐
 │ logique métier       │
 │ gestion participants │
 └──────────────────────┘
```

Cette organisation permet de répartir les responsabilités.

| Module                    | Responsabilité                     |
| ------------------------- | ---------------------------------- |
| `data.py`                 | Données initiales des participants |
| `data_menu.py`            | Données des menus                  |
| `affichage.py`            | Affichage                          |
| `gestion_participants.py` | Gestion des participants           |
| `statistiques.py`         | Calcul des statistiques            |
| `main.py`                 | Orchestration                      |

---

# 🎓 12. Intérêt pédagogique

La création de `data.py` constitue une étape importante dans l'apprentissage du **refactoring**.

L'apprenant découvre qu'un programme peut être décomposé en plusieurs responsabilités.

On passe progressivement de :

```text
CODE MONOLITHIQUE
       │
       ▼
    main.py
       │
       ▼
   tout mélangé
```

à :

```text
                 APPLICATION
                      │
       ┌──────────────┼──────────────┐
       ▼              ▼              ▼
    DONNÉES        AFFICHAGE      LOGIQUE
       │              │              │
       ▼              ▼              ▼
   data.py       affichage.py   fonctions
```

Cette étape prépare naturellement l'introduction des **fonctions** et des **modules**.

---

# 💡 13. Phrase pédagogique à retenir

> 📌 **`data.py` est un module de données : il initialise et centralise les ensembles de participants afin de séparer les données des menus, de l'affichage et de la logique de l'application.**

---

# 🚀 14. Étape suivante

Une fois `data.py` créé, nous pouvons nous intéresser à la manière dont les données sont utilisées.

Par exemple :

```python
from data import python, java, web
```

Puis créer des fonctions spécialisées :

```python
def afficher_participants(participants):
    ...
```

ou :

```python
def rechercher_participant(nom, participants):
    ...
```

ou encore :

```python
def participants_communs(groupe1, groupe2):
    ...
```

On franchit alors une nouvelle étape :

```text
DONNÉES
  ↓
data.py
  ↓
FONCTIONS
  ↓
LOGIQUE MÉTIER
  ↓
MODULES
  ↓
APPLICATION MODULAIRE
```

---

# 📌 À retenir

```text
                data.py
                   │
                   ▼
          ┌─────────────────┐
          │ Données initiales│
          └────────┬────────┘
                   │
        ┌──────────┼──────────┐
        ▼          ▼          ▼
     python      java        web
        │          │          │
        └──────────┼──────────┘
                   │
                   ▼
             autres modules
```

### Principe fondamental

**`data.py` contient les données.**

**Les fonctions utilisent les données.**

**Les modules organisent les responsabilités.**

**`main.py` orchestre l'application.**

C'est cette séparation progressive qui permet de transformer un programme initialement monolithique en une **application modulaire, plus lisible et plus facile à maintenir**.

Vous pouvez ainsi présenter `data.py` comme la **première brique de données** de votre architecture, puis `data_menu.py` comme la brique dédiée aux **données d'interface**, avant d'introduire `affichage.py` et les fonctions.
