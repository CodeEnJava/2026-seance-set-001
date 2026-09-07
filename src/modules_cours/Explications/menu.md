Voici le `README.md` du module `menu.py`, dans la continuité des précédents. Il met en évidence un point pédagogique important : **`menu.py` utilise les fonctions d'autres modules pour réaliser sa responsabilité d'affichage**, ce qui illustre déjà la collaboration entre modules.

# 📋 `menu.py` — Afficher et gérer les menus

## 🎯 Objectif

Le module `menu.py` a une responsabilité clairement définie :

> **Construire et afficher les menus de l'application et récupérer le choix de l'utilisateur.**

Il constitue le module chargé de l'**interface textuelle des menus**.

Il ne contient pas les données des menus, ne gère pas directement les participants et ne réalise pas les traitements métier.

Il utilise plusieurs fonctions provenant d'autres modules :

```python
from utils import clear_screen
from reader import read_integer_min_max
```

Cette organisation illustre un principe fondamental de la modularité :

> **Un module peut utiliser les services proposés par d'autres modules.**

---

# 🧩 1. Le rôle général de `menu.py`

Le module `menu.py` prend en charge la présentation des menus dans le terminal.

Il réalise principalement trois opérations :

```text id="menu-role"
          menu.py
             │
     ┌───────┼────────┐
     │       │        │
     ▼       ▼        ▼
  créer    afficher   lire
  titre     choix    choix
```

Ces responsabilités sont réparties dans trois fonctions :

| Fonction         | Responsabilité                               |
| ---------------- | -------------------------------------------- |
| `create_title()` | Construire et afficher le titre              |
| `create_items()` | Afficher les options du menu                 |
| `show_menu()`    | Coordonner l'affichage et récupérer le choix |

---

# 📦 2. Les dépendances du module

Au début du fichier, deux fonctions sont importées :

```python
from utils import clear_screen
from reader import read_integer_min_max
```

Le module `menu.py` ne réécrit donc pas ces fonctionnalités.

Il réutilise les fonctions déjà créées.

```text id="dependencies"
                 menu.py
                    │
          ┌─────────┴─────────┐
          │                   │
          ▼                   ▼
       utils.py           reader.py
          │                   │
          ▼                   ▼
   clear_screen()   read_integer_min_max()
```

Cette organisation permet d'éviter la duplication du code.

---

# 🧹 3. Utilisation de `clear_screen()`

La fonction :

```python
clear_screen()
```

provient du module `utils.py`.

Elle permet d'effacer le terminal avant d'afficher un nouveau menu.

Dans `show_menu()` :

```python
clear_screen()
```

Cela permet d'obtenir une interface plus propre.

Le module `menu.py` n'a pas besoin de connaître les détails techniques liés à Windows, Linux ou macOS.

Il demande simplement :

```python
clear_screen()
```

C'est `utils.py` qui se charge du travail technique.

---

# ⌨️ 4. Utilisation de `read_integer_min_max()`

La fonction :

```python
read_integer_min_max()
```

provient du module `reader.py`.

Elle permet de demander un entier à l'utilisateur et de vérifier que celui-ci appartient à l'intervalle attendu.

Dans `show_menu()` :

```python
return read_integer_min_max(
    "Votre choix : ",
    0,
    maxi=len(list_menu[1])
)
```

Le module `menu.py` délègue donc la validation de la saisie à `reader.py`.

On obtient une séparation claire :

```text id="separation"
menu.py
   │
   │ demande une saisie
   ▼
reader.py
   │
   │ valide la saisie
   ▼
valeur correcte
```

---

# 🏷️ 5. La fonction `create_title()`

La fonction :

```python
def create_title(str_title):
```

est responsable de la création graphique du titre du menu.

Elle reçoit un paramètre :

```text id="title-param"
str_title
```

qui correspond au texte du titre.

Par exemple :

```python
create_title("GESTION DES PARTICIPANTS")
```

produira un affichage de ce type :

```text id="title-output"
=================================
       GESTION DES PARTICIPANTS
=================================
```

---

# 📏 6. Calcul de la longueur du titre

La fonction commence par calculer la longueur du texte :

```python
len_title = len(str_title)
```

Puis elle utilise cette longueur pour adapter la largeur des lignes :

```python
print("=" * (14 + len_title))
```

Le titre est donc construit dynamiquement.

La fonction peut ainsi fonctionner avec des titres de longueurs différentes.

```text id="dynamic-title"
"MENU PRINCIPAL"
       │
       ▼
 longueur du texte
       │
       ▼
 largeur adaptée

"REQUÊTE D'AFFICHAGE DES PARTICIPANTS"
       │
       ▼
 longueur différente
       │
       ▼
 largeur adaptée
```

---

# 📋 7. La fonction `create_items()`

La fonction :

```python
def create_items(list_items):
```

est responsable de l'affichage des options du menu.

Elle reçoit une liste :

```text id="items"
list_items
    │
    ├── option 1
    ├── option 2
    ├── option 3
    └── ...
```

La fonction parcourt cette liste :

```python
for item in list_items:
```

et affiche chaque option.

---

# 🔢 8. La numérotation des choix

La variable :

```python
choix = 1
```

permet de numéroter les éléments.

L'affichage est construit avec :

```python
print(str(choix) + " - " + item)
```

On obtient par exemple :

```text id="items-output"
1 - Afficher les participants
2 - Ajouter un participant
3 - Supprimer un participant
4 - Rechercher un participant
5 - Participants communs
6 - Statistiques
0 - Quitter
```

Le dernier élément reçoit le choix `0`.

---

# 🔄 9. Pourquoi utiliser une boucle ?

Au lieu d'écrire :

```python
print("1 - Afficher les participants")
print("2 - Ajouter un participant")
print("3 - Supprimer un participant")
...
```

la fonction utilise une boucle :

```python
for item in list_items:
```

Cela permet d'afficher **n'importe quelle liste d'options**.

La fonction devient donc générique.

```text id="generic-items"
create_items(list_items)
          │
          ├── menu principal
          │
          ├── sous-menu
          │
          └── autre menu
```

---

# 🔀 10. Le choix `0` pour le dernier élément

Le code contient :

```python
if choix > len(list_items) - 1:
    choix = 0
```

Cela permet de faire en sorte que le dernier élément de la liste soit associé au choix `0`.

Par exemple, avec 7 éléments :

```text id="zero-choice"
1 → élément 1
2 → élément 2
3 → élément 3
4 → élément 4
5 → élément 5
6 → élément 6
0 → élément 7
```

Cette convention permet notamment d'utiliser `0` pour une option telle que :

```text
Quitter
```

ou :

```text
Retour au menu principal
```

---

# 🎛️ 11. La fonction `show_menu()`

La fonction principale du module est :

```python
def show_menu(list_menu):
```

Elle reçoit la structure complète d'un menu.

Par exemple :

```python
main_menu
```

ou :

```python
sub_menu
```

Son rôle est de coordonner les différentes étapes :

```text id="show-menu-flow"
show_menu(list_menu)
        │
        ▼
  effacer l'écran
        │
        ▼
   afficher le titre
        │
        ▼
   afficher les options
        │
        ▼
   demander le choix
        │
        ▼
 retourner le choix
```

---

# 🔗 12. Une fonction qui utilise d'autres fonctions

`show_menu()` est particulièrement intéressante dans une démarche pédagogique.

Elle utilise :

```python
clear_screen()
```

puis :

```python
create_title()
```

puis :

```python
create_items()
```

et enfin :

```python
read_integer_min_max()
```

On obtient une véritable **composition de fonctions** :

```text id="function-composition"
                 show_menu()
                      │
       ┌──────────────┼──────────────┐
       ▼              ▼              ▼
clear_screen()  create_title()  create_items()
                                      │
                                      ▼
                           read_integer_min_max()
```

Chaque fonction réalise une tâche précise.

`show_menu()` orchestre ces différentes tâches.

---

# 📦 13. La structure `list_menu`

La fonction `show_menu()` attend une structure composée de deux éléments :

```text id="list-menu"
list_menu
   │
   ├── [0] → titre
   │
   └── [1] → liste des options
```

Cette structure correspond directement aux données définies dans `data_menu.py`.

Par exemple :

```python
main_menu = [
    "GESTION DES PARTICIPANTS",
    main_items
]
```

Ainsi :

```python
list_menu[0]
```

correspond au titre.

Et :

```python
list_menu[1]
```

correspond à la liste des choix.

---

# 🔄 14. Collaboration avec `data_menu.py`

Les responsabilités sont maintenant bien séparées.

```text id="menu-data-collaboration"
             data_menu.py
                  │
                  │ fournit
                  ▼
              main_menu
                  │
                  ▼
               menu.py
                  │
        ┌─────────┼─────────┐
        ▼         ▼         ▼
     titre      items      saisie
        │         │         │
        ▼         ▼         ▼
 create_title  create_items  reader.py
```

`data_menu.py` fournit les données.

`menu.py` les présente.

C'est une séparation importante entre :

> **les données et leur utilisation.**

---

# 🏗️ 15. Avant le refactoring

Avant la création de `menu.py`, le programme principal pouvait contenir directement :

```python
print("=" * 40)
print("GESTION DES PARTICIPANTS")
print("=" * 40)

print("1 - Afficher les participants")
print("2 - Ajouter un participant")
print("3 - Supprimer un participant")
...
```

Le programme principal mélangeait alors :

```text id="before-menu"
┌─────────────────────────────┐
│          main.py            │
├─────────────────────────────┤
│ Données                     │
│ Menus                       │
│ Affichage                   │
│ Saisies                     │
│ Traitements                 │
│ Statistiques                │
└─────────────────────────────┘
```

---

# ✨ 16. Après le refactoring

Après création des différents modules :

```text id="after-menu"
                      main.py
                         │
          ┌──────────────┼──────────────┐
          ▼              ▼              ▼
      data.py       data_menu.py      menu.py
          │              │              │
          │              │              ├── create_title()
          │              │              ├── create_items()
          │              │              └── show_menu()
          │              │
          │              ▼
          │          données menus
          │
          ▼
    données participants
```

Le programme principal peut maintenant utiliser ces fonctionnalités sans connaître leur implémentation détaillée.

---

# ♻️ 17. Réutilisabilité

L'intérêt majeur de `menu.py` est que les fonctions peuvent être utilisées avec plusieurs menus.

Par exemple :

```python
show_menu(main_menu)
```

puis :

```python
show_menu(sub_menu)
```

La même fonction est utilisée dans les deux cas.

```text id="reusability"
                    show_menu()
                        │
              ┌─────────┴─────────┐
              ▼                   ▼
          main_menu           sub_menu
              │                   │
              ▼                   ▼
       Menu principal        Sous-menu
```

Il n'est donc pas nécessaire de créer :

```python
show_main_menu()
show_sub_menu()
```

Une seule fonction générique suffit.

---

# 🎯 18. Une responsabilité clairement identifiée

Le rôle de `menu.py` est :

> **Gérer la présentation et la sélection des menus de l'application.**

Il ne doit pas :

```text id="menu-not-responsible"
❌ stocker les données des participants
❌ définir les données des menus
❌ gérer les participants
❌ calculer les statistiques
❌ décider de la logique métier
```

Il doit :

```text id="menu-responsible"
✅ construire les titres
✅ afficher les options
✅ présenter le menu
✅ demander le choix de l'utilisateur
✅ retourner le choix
```

---

# 🧠 19. Une distinction importante

Il est intéressant de distinguer trois responsabilités :

```text id="three-responsibilities"
DONNÉES
   │
   ▼
data_menu.py
   │
   │ fournit le menu
   ▼
AFFICHAGE
   │
   ▼
menu.py
   │
   │ demande le choix
   ▼
reader.py
   │
   ▼
SAISIE VALIDÉE
```

Ainsi :

* `data_menu.py` **définit** ;
* `menu.py` **affiche** ;
* `reader.py` **lit et valide**.

Cette séparation est au cœur de la modularité.

---

# 📚 20. Les responsabilités des modules

L'architecture de l'application devient progressivement :

| Module                    | Responsabilité                           |
| ------------------------- | ---------------------------------------- |
| `data.py`                 | Initialiser les données des participants |
| `data_menu.py`            | Définir les données des menus            |
| `utils.py`                | Fournir des fonctions utilitaires        |
| `reader.py`               | Lire et valider les saisies              |
| `menu.py`                 | Construire et afficher les menus         |
| `affichage.py`            | Afficher les résultats de l'application  |
| `gestion_participants.py` | Gérer les participants                   |
| `statistiques.py`         | Calculer les statistiques                |
| `main.py`                 | Orchestrer l'application                 |

Chaque module possède ainsi une responsabilité spécifique.

---

# 🎓 21. Intérêt pédagogique

`menu.py` permet d'introduire plusieurs notions importantes :

### 1. Les fonctions

```python
create_title()
create_items()
show_menu()
```

Chaque fonction possède une responsabilité précise.

### 2. Les paramètres

```python
create_title(str_title)
```

et :

```python
create_items(list_items)
```

permettent aux fonctions de travailler avec différentes données.

### 3. La réutilisation

```python
show_menu(main_menu)
show_menu(sub_menu)
```

Une même fonction peut gérer plusieurs situations.

### 4. La composition

`show_menu()` utilise plusieurs fonctions spécialisées.

### 5. Les modules

`menu.py` utilise :

```python
utils.py
reader.py
data_menu.py
```

Les différents modules collaborent sans mélanger leurs responsabilités.

---

# 🔄 22. La démarche de refactoring

Le chemin parcouru peut être résumé ainsi :

```text id="refactoring-path"
PROGRAMME INITIAL
      │
      ▼
  code monolithique
      │
      ▼
identifier les responsabilités
      │
      ▼
créer des fonctions
      │
      ▼
regrouper les fonctions
      │
      ▼
créer des modules
      │
      ▼
faire communiquer les modules
      │
      ▼
APPLICATION MODULAIRE
```

Pour `menu.py`, la démarche est :

```text id="menu-refactoring"
Afficher un menu
      │
      ▼
identifier plusieurs tâches
      │
      ├── créer le titre
      ├── afficher les options
      └── lire le choix
             │
             ▼
        créer des fonctions
             │
             ▼
           menu.py
```

---

# 💡 23. Phrase pédagogique à retenir

> 📌 **`menu.py` est un module d'interface : il construit et affiche les menus de l'application et utilise des fonctions spécialisées pour effacer l'écran et valider les saisies utilisateur.**

On peut également résumer son fonctionnement par :

> **`data_menu.py` fournit les données → `menu.py` les affiche → `reader.py` valide le choix.**

---

# 🚀 24. Étape suivante

Avec `menu.py`, une étape importante de la modularisation est franchie.

Nous avons maintenant séparé :

```text id="next-step"
data.py
    ↓
Données participants

data_menu.py
    ↓
Données menus

utils.py
    ↓
Outils techniques

reader.py
    ↓
Saisie utilisateur

menu.py
    ↓
Affichage et gestion des menus
```

Il reste ensuite à isoler la **logique métier** de l'application.

Par exemple :

```text id="business-logic"
gestion_participants.py
        │
        ├── ajouter_participant()
        ├── supprimer_participant()
        ├── rechercher_participant()
        └── participants_communs()
```

Puis `main.py` pourra simplement orchestrer l'ensemble.

---

# 📌 À retenir

```text id="summary"
                         APPLICATION
                              │
                              ▼
                           main.py
                              │
                              ▼
                           menu.py
                              │
             ┌────────────────┼────────────────┐
             ▼                ▼                ▼
       data_menu.py       utils.py        reader.py
             │                │                │
             ▼                ▼                ▼
       données menus     effacer écran    valider saisie
```

### Principe fondamental

**`data_menu.py` définit les données.**

**`menu.py` présente les menus.**

**`reader.py` valide les saisies.**

**`utils.py` fournit les outils techniques.**

**`main.py` orchestre les différents modules.**

Cette organisation permet de passer progressivement d'un programme monolithique à une **application Python modulaire, lisible, réutilisable et maintenable**.
