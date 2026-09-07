Voici un `README.md` prêt à intégrer dans votre dépôt GitHub, structuré pour rester cohérent avec votre démarche pédagogique **Refactoring → Fonctions → Modularité**.

# 📋 `data_menu.py` — Centraliser les données des menus

## 🎯 Objectif

Le module `data_menu.py` a un rôle très précis :

> **Centraliser les données utilisées pour construire les menus de l'application.**

Dans une démarche de **refactoring** et de **modularité**, l'objectif est de séparer progressivement les différentes responsabilités du programme :

```text
┌─────────────────────────────────────────┐
│             APPLICATION                 │
└────────────────────┬────────────────────┘
                     │
          ┌──────────┼──────────┐
          │          │          │
          ▼          ▼          ▼
       DONNÉES    AFFICHAGE   LOGIQUE
          │          │          │
          ▼          ▼          ▼
  data_menu.py  affichage.py  fonctions
```

Cette séparation permet d'obtenir un code **plus lisible, plus maintenable et plus évolutif**.

---

# 🧩 1. Le rôle général de `data_menu.py`

On peut considérer `data_menu.py` comme un **catalogue des menus** de l'application.

Il contient uniquement les **données statiques** nécessaires à la construction des menus.

Il ne contient :

* ❌ aucune saisie utilisateur ;
* ❌ aucun affichage à l'écran ;
* ❌ aucun calcul ;
* ❌ aucune logique métier ;
* ❌ aucune gestion des participants.

Il fournit simplement des données aux autres modules.

```text
                  APPLICATION
                       │
                       ▼
              ┌─────────────────┐
              │  data_menu.py   │
              └────────┬────────┘
                       │
             données des menus
                       │
              ┌────────┴────────┐
              ▼                 ▼
       Menu principal     Sous-menu
```

Cette responsabilité unique constitue une première étape vers une meilleure **modularité**.

---

# 📋 2. Le menu principal

Le titre du menu est défini dans une variable :

```python
main_title = "GESTION DES PARTICIPANTS"
```

Les différentes options sont regroupées dans une liste :

```python
main_items = [
    "Afficher les participants",
    "Ajouter un participant",
    "Supprimer un participant",
    "Rechercher un participant",
    "Participants communs",
    "Statistiques",
    "Quitter"
]
```

On peut ensuite regrouper le titre et les options :

```python
main_menu = [main_title.upper(), main_items]
```

La structure obtenue peut être représentée ainsi :

```text
main_menu
│
├── titre
│     └── "GESTION DES PARTICIPANTS"
│
└── items
      ├── Afficher les participants
      ├── Ajouter un participant
      ├── Supprimer un participant
      ├── Rechercher un participant
      ├── Participants communs
      ├── Statistiques
      └── Quitter
```

Le module `data_menu.py` ne se préoccupe pas de **comment** ce menu sera affiché.

Il fournit uniquement les données.

---

# 📂 3. Le sous-menu

Le même principe est utilisé pour le sous-menu.

Le titre est défini par :

```python
sub_title = "Requête d'affichage des participants"
```

Les différentes options sont regroupées dans une liste :

```python
sub_items = [
    "Afficher les participants du groupe Python",
    "Afficher les participants du groupe Java",
    "Afficher les participants du groupe Web",
    "Afficher les participants de tous les groupes",
    "Afficher les participants en fonction d'une requête",
    "Retour au menu principal"
]
```

Puis les deux informations sont regroupées :

```python
sub_menu = [sub_title.upper(), sub_items]
```

La structure devient :

```text
sub_menu
│
├── titre
│     └── "REQUÊTE D'AFFICHAGE DES PARTICIPANTS"
│
└── items
      ├── Afficher les participants du groupe Python
      ├── Afficher les participants du groupe Java
      ├── Afficher les participants du groupe Web
      ├── Afficher les participants de tous les groupes
      ├── Afficher les participants en fonction d'une requête
      └── Retour au menu principal
```

---

# 🔄 4. Pourquoi créer un module spécifique ?

Sans `data_menu.py`, toutes les données des menus pourraient être directement placées dans `main.py`.

Le programme principal contiendrait alors progressivement :

```text
┌─────────────────────────────┐
│          main.py            │
├─────────────────────────────┤
│ Données des menus           │
│ Affichage                   │
│ Saisies utilisateur         │
│ Traitements                 │
│ Gestion des participants    │
│ Statistiques                │
└─────────────────────────────┘
```

Le fichier principal deviendrait rapidement difficile à comprendre et à maintenir.

---

# 🛠️ 5. Après refactoring

Avec la modularisation, les responsabilités sont réparties entre plusieurs modules :

```text
                 ┌─────────────────────┐
                 │      main.py        │
                 │                     │
                 │   orchestration     │
                 └──────────┬──────────┘
                            │
            ┌───────────────┼───────────────┐
            │               │               │
            ▼               ▼               ▼
 ┌────────────────┐ ┌───────────────┐ ┌─────────────────┐
 │ data_menu.py   │ │ affichage.py  │ │ gestion_        │
 │                │ │               │ │ participants.py │
 │ Données menus  │ │ afficher_menu │ │ Logique métier  │
 └────────────────┘ └───────────────┘ └─────────────────┘
```

Chaque module possède alors une responsabilité clairement identifiée.

| Module                    | Responsabilité                |
| ------------------------- | ----------------------------- |
| `data_menu.py`            | Définir les données des menus |
| `affichage.py`            | Afficher les menus            |
| `gestion_participants.py` | Gérer les participants        |
| `statistiques.py`         | Calculer les statistiques     |
| `main.py`                 | Orchestrer l'application      |

---

# 🎯 6. Séparer les données et l'affichage

Cette séparation est particulièrement intéressante lorsqu'on introduit les **fonctions**.

Le module `data_menu.py` fournit :

```python
main_menu
sub_menu
```

Le module `affichage.py` peut alors proposer une fonction générique :

```python
def afficher_menu(menu):
    ...
```

Cette fonction peut recevoir différents menus :

```python
afficher_menu(main_menu)
```

ou :

```python
afficher_menu(sub_menu)
```

On évite ainsi de créer une fonction différente pour chaque menu.

```text
             data_menu.py
                  │
       ┌──────────┴──────────┐
       │                     │
       ▼                     ▼
   main_menu             sub_menu
       │                     │
       └──────────┬──────────┘
                  ▼
           afficher_menu()
                  │
                  ▼
              Écran
```

C'est ici que l'on commence à voir concrètement l'intérêt de la **factorisation du code par les fonctions**.

---

# 🧠 7. Une responsabilité unique

Le principe peut être résumé simplement :

> **Un module doit avoir une responsabilité clairement identifiée.**

La responsabilité de `data_menu.py` est :

> **Définir et centraliser les données nécessaires aux menus de l'application.**

Il ne doit donc pas :

```text
❌ afficher les menus
❌ demander un choix à l'utilisateur
❌ traiter le choix
❌ modifier les participants
❌ calculer des statistiques
```

Il doit simplement :

```text
✅ définir les titres
✅ définir les options
✅ organiser les données des menus
```

---

# 🏗️ 8. Une première étape vers l'architecture modulaire

La création de `data_menu.py` peut sembler très simple.

Pourtant, elle constitue une étape importante dans le refactoring.

On passe progressivement de :

```text
                  MONOLITHE
                     │
                     ▼
              ┌─────────────┐
              │   main.py   │
              │             │
              │ tout mélangé│
              └─────────────┘
```

à :

```text
                  APPLICATION
                       │
        ┌──────────────┼──────────────┐
        │              │              │
        ▼              ▼              ▼
     DONNÉES       AFFICHAGE       LOGIQUE
        │              │              │
        ▼              ▼              ▼
 data_menu.py    affichage.py   gestion_*.py
```

Chaque nouveau module permet ainsi de **réduire la complexité du programme principal**.

---

# 🎓 9. Intérêt pédagogique

Dans une séance consacrée au :

```text
REFACTORING
     ↓
FONCTIONS
     ↓
MODULARITÉ
```

`data_menu.py` constitue une excellente transition.

L'apprenant découvre progressivement que :

1. toutes les instructions n'ont pas nécessairement leur place dans `main.py` ;
2. les données peuvent être séparées du traitement ;
3. l'affichage peut être confié à des fonctions ;
4. la logique métier peut être isolée ;
5. plusieurs modules peuvent collaborer pour construire une application.

---

# 💡 10. Phrase pédagogique à retenir

> 📌 **`data_menu.py` est un module de données : il centralise les titres et les choix des menus afin de séparer les données de leur affichage et de la logique de l'application.**

Cette phrase résume parfaitement le rôle du module.

---

# 🚀 11. Étape suivante

Après avoir créé `data_menu.py`, l'étape suivante consiste à créer :

```text
affichage.py
```

et à y placer une fonction générique :

```python
def afficher_menu(menu):
    ...
```

L'objectif sera alors de montrer qu'une **même fonction** peut afficher :

```python
main_menu
```

mais également :

```python
sub_menu
```

On passe ainsi naturellement de la **séparation des données** à la **création de fonctions réutilisables**, puis à la **modularité de l'application**.

---

## 📌 À retenir

```text
data_menu.py
     │
     │  contient
     ▼
DONNÉES DES MENUS
     │
     │  utilisées par
     ▼
affichage.py
     │
     │  utilise
     ▼
fonction afficher_menu()
     │
     ▼
APPLICATION MODULAIRE
```

### Principe fondamental

**Les données ne sont pas l'affichage.**

**L'affichage n'est pas la logique métier.**

**La logique métier n'est pas l'orchestration.**

La modularité consiste précisément à **séparer ces responsabilités**.

Ce README peut servir directement de **support pédagogique GitHub** pour votre séance. Il prépare naturellement la prochaine étape : `affichage.py` et la création de `afficher_menu(menu)`.
