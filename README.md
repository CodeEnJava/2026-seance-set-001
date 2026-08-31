# 2026-seance-dico-set-001
# 🎯 Mini-projet — Analyse des participants avec les ensembles

**S-PYTH — Les ensembles (`set`) en Python**

---

## 📚 Présentation

Ce mini-projet propose de mettre en pratique les **ensembles (`set`) en Python** à travers la réalisation d'un programme permettant de gérer les participants à plusieurs activités.

Une association propose différentes activités :

* 🐍 Python
* ☕ Java
* 🌐 Web

Chaque activité possède son propre ensemble de participants.

Le programme devra permettre d'exploiter ces ensembles afin d'effectuer différentes opérations :

* rechercher un participant ;
* compter les participants ;
* ajouter ou supprimer un participant ;
* déterminer l'ensemble des participants ;
* rechercher les participants communs à plusieurs activités ;
* identifier les participants présents dans une activité mais pas dans une autre ;
* analyser les inscriptions aux différentes activités.

L'objectif du projet est avant tout de **comprendre et manipuler les ensembles Python ainsi que leurs opérations**.

---

## 🎯 Objectifs pédagogiques

À l'issue de ce mini-projet, l'apprenant doit être capable de :

* créer un ensemble avec Python ;
* ajouter des éléments dans un ensemble ;
* supprimer des éléments ;
* rechercher un élément ;
* parcourir un ensemble ;
* compter les éléments d'un ensemble ;
* comprendre la notion d'unicité des éléments ;
* effectuer des opérations entre ensembles ;
* utiliser l'union ;
* utiliser l'intersection ;
* utiliser la différence ;
* utiliser la différence symétrique ;
* exploiter les ensembles dans un problème concret.

---

## 🧠 Compétences travaillées

### Ensembles

* `set`
* création d'un ensemble ;
* ajout avec `add()` ;
* suppression avec `remove()` et `discard()` ;
* recherche avec `in` ;
* parcours avec `for` ;
* comptage avec `len()`.

### Opérations sur les ensembles

| Opération             | Opérateur | Méthode                  | Description                                           |
| --------------------- | --------: | ------------------------ | ----------------------------------------------------- |
| Union                 |      `\|` | `union()`                | Réunit les éléments des ensembles                     |
| Intersection          |       `&` | `intersection()`         | Éléments communs                                      |
| Différence            |       `-` | `difference()`           | Éléments présents dans le premier ensemble uniquement |
| Différence symétrique |       `^` | `symmetric_difference()` | Éléments présents dans un seul des deux ensembles     |

---

## 🏫 Contexte du projet

Une association organise trois activités :

```text
Python
Java
Web
```

Les participants sont représentés par leur prénom.

Exemple :

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
    "Emma",
    "Franck",
    "Gérard"
}
```

Ces ensembles serviront de base aux différentes analyses demandées dans le projet.

---

## 📋 Travail demandé

Le programme devra progressivement permettre de réaliser les opérations suivantes.

### 1. Afficher les participants

Afficher les participants inscrits à chaque activité.

### 2. Compter les participants

Afficher le nombre de participants pour chaque activité à l'aide de `len()`.

### 3. Rechercher un participant

Demander un prénom à l'utilisateur et déterminer si cette personne est inscrite à une ou plusieurs activités.

### 4. Déterminer tous les participants

Utiliser l'**union** des ensembles afin d'obtenir la liste des personnes participant à au moins une activité.

```python
python | java | web
```

### 5. Rechercher les participants communs

Déterminer les participants communs à deux activités.

```python
python & java
```

Puis rechercher les personnes participant aux trois activités :

```python
python & java & web
```

### 6. Utiliser la différence

Déterminer les participants inscrits à Python mais pas à Java :

```python
python - java
```

Puis effectuer l'opération inverse :

```python
java - python
```

### 7. Utiliser la différence symétrique

Identifier les personnes participant à une seule des deux activités :

```python
python ^ java
```

### 8. Ajouter un participant

Demander à l'utilisateur le nom d'un participant et l'activité à laquelle il souhaite s'inscrire.

Utiliser :

```python
add()
```

### 9. Supprimer un participant

Permettre de supprimer un participant d'une activité.

Utiliser notamment :

```python
discard()
```

### 10. Produire un bilan

Afficher une synthèse des inscriptions et des différentes analyses réalisées.

---

# 🚫 Contraintes du projet

Afin de respecter l'objectif pédagogique de la séance, le projet doit respecter les contraintes suivantes :

* ❌ ne pas utiliser `def` ;
* ❌ ne pas créer de fonction personnelle ;
* ❌ ne pas créer de classe ;
* ❌ ne pas utiliser de bibliothèque externe ;
* ❌ ne pas créer de module personnel ;
* ✅ utiliser les ensembles `set` ;
* ✅ utiliser les opérations entre ensembles ;
* ✅ utiliser les conditions ;
* ✅ utiliser les boucles ;
* ✅ utiliser `input()` pour les interactions avec l'utilisateur.

### ⚠️ Une contrainte volontaire

L'absence de fonctions est **volontaire**.

Le but de ce projet est de se concentrer sur :

> **la compréhension et la manipulation des ensembles en Python.**

La création de fonctions et la modularisation du programme feront l'objet d'une **séance dédiée**.

Lors de cette future étape, le programme pourra être repris et découpé en différentes fonctions afin d'améliorer :

* la lisibilité ;
* la maintenance ;
* la réutilisation du code ;
* l'évolution du programme.

---

# 📁 Organisation du projet

Une organisation simple peut être utilisée :

```text
mini-projet-ensembles/
│
├── README.md
│
└── src/
    └── participants.py
```

Le fichier `participants.py` contient l'ensemble du programme.

---

# ▶️ Exécution

## Prérequis

* Python 3.x
* Un éditeur de code ou un IDE :

  * PyCharm
  * Visual Studio Code
  * IDLE
  * ou tout autre environnement Python.

## Exécution depuis un terminal

Depuis le répertoire du projet :

```bash
python src/participants.py
```

Sous Windows, il peut également être nécessaire d'utiliser :

```bash
py src/participants.py
```

---

# 💡 Exemple de résultat attendu

Le programme pourra produire un affichage similaire à :

```text
========================================
       GESTION DES PARTICIPANTS
========================================

Python : 5 participants
Java   : 4 participants
Web    : 5 participants

Nombre total de participants : 7

----------------------------------------
Participants Python et Java
----------------------------------------

Bob
David
Emma

----------------------------------------
Participants aux trois activités
----------------------------------------

Emma
```

> ℹ️ L'ordre d'affichage des éléments d'un ensemble n'est pas garanti. L'ordre des prénoms peut donc être différent d'une exécution à l'autre.

---

# 🔎 Notion importante : l'unicité

Un ensemble ne conserve qu'une seule occurrence d'un élément.

Par exemple :

```python
participants = {
    "Alice",
    "Bob",
    "Alice"
}
```

Le résultat contient seulement :

```text
Alice
Bob
```

Cela constitue l'un des principaux intérêts des ensembles lorsqu'il est nécessaire de manipuler des données **sans doublons**.

---

# 🧪 Pistes de tests

Le programme devra être testé avec différents scénarios.

### Test 1 — Recherche

Rechercher :

```text
Emma
```

Vérifier qu'elle est présente dans les trois activités.

### Test 2 — Recherche d'un participant inexistant

Rechercher :

```text
Paul
```

Vérifier que le programme indique qu'il n'est inscrit à aucune activité.

### Test 3 — Ajout

Ajouter :

```text
Paul
```

à l'activité Python.

Vérifier que le nombre de participants augmente.

### Test 4 — Ajout d'un participant déjà présent

Ajouter à nouveau :

```text
Paul
```

Vérifier le comportement d'un `set`.

### Test 5 — Suppression

Supprimer un participant d'une activité puis vérifier que l'ensemble a bien été modifié.

---

# ⭐ Défis

Une fois le programme principal terminé, plusieurs défis peuvent être proposés.

## Défi 1 — Participants aux trois activités

Afficher les personnes inscrites simultanément à :

* Python ;
* Java ;
* Web.

---

## Défi 2 — Participants à une seule activité

Déterminer les personnes qui participent à **une seule activité**.

---

## Défi 3 — Statistiques

Afficher :

* le nombre total de participants ;
* le nombre de participants par activité ;
* le nombre de participants aux trois activités ;
* le nombre de participants à plusieurs activités.

---

## Défi 4 — Menu

Créer un menu permettant de choisir une opération :

```text
========================================
       GESTION DES PARTICIPANTS
========================================

1 - Afficher les participants
2 - Ajouter un participant
3 - Supprimer un participant
4 - Rechercher un participant
5 - Participants communs
6 - Statistiques
0 - Quitter

Votre choix :
```

Le menu pourra être réalisé avec une boucle `while`.

> ⚠️ Toujours sans créer de fonction.

---

# 🚀 Évolution vers la modularité

Une fois le projet terminé, une nouvelle version pourra être réalisée.

L'objectif sera de reprendre le programme et de transformer le code monolithique en un programme **modulaire**.

Par exemple :

```text
participants.py
│
├── afficher_participants()
├── ajouter_participant()
├── supprimer_participant()
├── rechercher_participant()
├── calculer_statistiques()
└── afficher_menu()
```

Cette seconde version permettra d'introduire progressivement :

* les fonctions ;
* les paramètres ;
* les valeurs de retour ;
* la réutilisation du code ;
* le découpage en modules ;
* la maintenance ;
* l'évolution d'une application.

Ainsi, les deux projets pourront être comparés :

```text
Projet 1
Ensembles
    ↓
Programme linéaire
    ↓
Comprendre les structures de données
    ↓
Projet 2
Fonctions et modularité
    ↓
Découpage du programme
    ↓
Maintenance et évolution
```

---

# 📊 Critères d'évaluation

| Critère                                      | Points |
| -------------------------------------------- | -----: |
| Création et utilisation des ensembles        |      4 |
| Utilisation des opérations sur les ensembles |      5 |
| Recherche et manipulation des participants   |      3 |
| Utilisation des boucles et conditions        |      3 |
| Interaction avec l'utilisateur               |      2 |
| Respect des contraintes                      |      2 |
| Lisibilité du code                           |      1 |
| **Total**                                    | **20** |

---

# 🎓 Bilan pédagogique

Ce mini-projet permet de mettre en application les principales caractéristiques des **ensembles Python** dans une situation concrète.

L'apprenant doit notamment comprendre que les ensembles sont particulièrement adaptés lorsqu'il est nécessaire de :

* supprimer les doublons ;
* tester rapidement l'appartenance d'un élément ;
* comparer plusieurs groupes de données ;
* rechercher des éléments communs ;
* déterminer les différences entre plusieurs groupes.

La structure volontairement **non modulaire** du programme constitue également un point pédagogique important.

> **On apprend d'abord à résoudre le problème avec les structures de données étudiées, puis on apprend à organiser et maintenir le code.**

La prochaine étape pourra donc naturellement être consacrée aux **fonctions et à la modularité**.

---

## 📌 Mots-clés

`Python` · `set` · `ensembles` · `union` · `intersection` · `difference` · `symmetric_difference` · `add` · `discard` · `boucles` · `conditions` · `input` · `algorithmique` · `programmation`

---

## 👨‍🏫 Séquence pédagogique

**Thématique :** Les ensembles en Python
**Type :** Mini-projet pratique
**Niveau :** Débutant
**Langage :** Python 3
**Structure :** Programme monolithique volontairement sans fonctions
**Objectif principal :** Manipuler et exploiter les ensembles Python
