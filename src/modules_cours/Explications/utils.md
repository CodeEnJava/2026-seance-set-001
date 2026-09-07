Voici le `README.md` pour `utils.py`, dans la continuité des modules `data.py`, `data_menu.py` et `reader.py`. J'ai mis l'accent sur la notion de **fonction utilitaire réutilisable** et sur l'intérêt de ce module dans plusieurs projets.

# 🛠️ `utils.py` — Fonctions utilitaires

## 🎯 Objectif

Le module `utils.py` regroupe des **fonctions utilitaires**, c'est-à-dire des fonctions qui réalisent des opérations techniques pouvant être réutilisées par différentes parties de l'application, voire par d'autres projets.

Dans cette application, `utils.py` contient une fonction :

```python
clear_screen()
```

Cette fonction a une responsabilité précise :

> **Effacer l'écran du terminal, quel que soit le système d'exploitation utilisé.**

---

# 🧩 1. Le rôle général de `utils.py`

Contrairement à un module contenant des données ou de la logique métier, `utils.py` regroupe des **outils génériques**.

Son rôle est de fournir des fonctions techniques réutilisables.

```text
                  APPLICATION
                       │
                       ▼
                ┌────────────┐
                │  utils.py  │
                └─────┬──────┘
                      │
                      ▼
               clear_screen()
                      │
          ┌───────────┴───────────┐
          ▼                       ▼
      Windows                  Linux / macOS
          │                       │
          ▼                       ▼
         cls                    clear
```

Le module n'est pas spécifique à la gestion des participants.

Il pourra donc être utilisé dans **d'autres projets Python**.

---

# 🧹 2. La fonction `clear_screen()`

La fonction est définie ainsi :

```python
def clear_screen():
```

Elle ne reçoit aucun paramètre.

Son objectif est simplement d'effacer le contenu actuellement affiché dans le terminal.

Exemple d'utilisation :

```python
clear_screen()
```

La fonction ne retourne aucune information utile :

```text
clear_screen()
      │
      ▼
efface le terminal
      │
      ▼
   return None
```

---

# 💻 3. Le problème de la compatibilité des systèmes

La commande permettant d'effacer l'écran dépend du système d'exploitation.

### Windows

La commande utilisée est :

```text
cls
```

### Linux et macOS

La commande utilisée est :

```text
clear
```

Il serait donc possible d'écrire directement dans le programme :

```python
import os

os.system("cls")
```

ou :

```python
os.system("clear")
```

Mais il faut alors gérer les différents systèmes d'exploitation.

`utils.py` permet de centraliser cette particularité technique.

---

# 🔍 4. Identifier le système d'exploitation

Le module utilise :

```python
import platform
```

La fonction :

```python
platform.system()
```

permet de connaître le système utilisé.

Par exemple :

```python
platform.system()
```

peut retourner :

```text
Windows
```

ou :

```text
Darwin
```

pour macOS, ou encore :

```text
Linux
```

La fonction peut donc déterminer quelle commande utiliser.

---

# ⚙️ 5. La condition

Le code contient :

```python
if platform.system() == "Windows":
    subprocess.run("cl", shell=True)
else:
    subprocess.run("clear", shell=True)
```

Le fonctionnement est donc :

```text
             platform.system()
                    │
          ┌─────────┴─────────┐
          │                   │
       Windows          autre système
          │                   │
          ▼                   ▼
       "cls"               "clear"
          │                   │
          └─────────┬─────────┘
                    ▼
             terminal effacé
```

---

# 🔧 6. Le module `subprocess`

Le module utilise également :

```python
import subprocess
```

La fonction :

```python
subprocess.run()
```

permet d'exécuter une commande du système.

Dans notre cas :

```python
subprocess.run("cl", shell=True)
```

sur Windows.

Et :

```python
subprocess.run("clear", shell=True)
```

sur Linux ou macOS.

La fonction `clear_screen()` masque donc ces détails techniques au reste de l'application.

---

# 🧱 7. Le code complet

Le module `utils.py` peut être présenté ainsi :

```python
import platform
import subprocess

# Module N°2
# Sa responsabilité : l'effacement de l'écran du terminal
# Ce module pourra être utilisé dans d'autre projet

def clear_screen():
    '''
    Cette fonction a pour but d'effacer l'écran du terminal
    :return: None
    '''
    if platform.system() == "Windows":
        subprocess.run("cl", shell=True)
    else:
        subprocess.run("clear", shell=True)
```

---

# 🔄 8. Avant le refactoring

Sans `utils.py`, le code permettant d'effacer l'écran pourrait être directement présent dans `main.py`.

On pourrait alors retrouver plusieurs fois :

```python
if platform.system() == "Windows":
    subprocess.run("cl", shell=True)
else:
    subprocess.run("clear", shell=True)
```

Le programme principal devrait alors connaître les détails techniques liés au système d'exploitation.

```text
                         main.py
                            │
          ┌─────────────────┼─────────────────┐
          │                 │                 │
          ▼                 ▼                 ▼
      affichage         saisies          clear screen
                                            │
                                      gestion Windows
                                            │
                                      gestion Linux
                                            │
                                      gestion macOS
```

Le fichier principal devient progressivement plus complexe.

---

# ✨ 9. Après le refactoring

Avec `utils.py`, toute cette logique est regroupée dans une seule fonction :

```python
clear_screen()
```

Le programme appelant n'a plus besoin de connaître les détails techniques.

Il lui suffit d'importer la fonction :

```python
from utils import clear_screen
```

Puis :

```python
clear_screen()
```

C'est tout.

```text
                 main.py
                    │
                    │ clear_screen()
                    ▼
               ┌─────────┐
               │ utils.py│
               └────┬────┘
                    │
              identification
              du système
                    │
          ┌─────────┴─────────┐
          ▼                   ▼
       Windows          Linux / macOS
          │                   │
          ▼                   ▼
         cls                 clear
```

---

# ♻️ 10. Une fonction réutilisable

L'un des principaux intérêts de `utils.py` est la **réutilisabilité**.

La fonction :

```python
clear_screen()
```

peut être appelée depuis plusieurs modules.

Par exemple :

```python
from utils import clear_screen
```

Puis :

```python
clear_screen()
```

Elle peut être utilisée :

* après l'affichage d'un menu ;
* avant l'affichage d'un nouveau menu ;
* après une opération ;
* avant l'affichage d'un résultat ;
* dans un autre projet Python.

On évite ainsi de recopier le même code.

---

# 🎯 11. Une responsabilité technique

`utils.py` possède une responsabilité différente de celle des autres modules.

Il ne contient pas les données des participants.

Il ne gère pas les menus.

Il ne réalise pas les traitements métier.

Il fournit des **services techniques génériques**.

```text
data.py
    ↓
Données

data_menu.py
    ↓
Données des menus

reader.py
    ↓
Lecture des saisies

utils.py
    ↓
Fonctions techniques réutilisables
```

Cette distinction permet de mieux organiser le projet.

---

# 🧠 12. Pourquoi appeler le module `utils.py` ?

Le terme `utils` est une abréviation de **utilities**.

Un module `utils.py` est généralement utilisé pour regrouper des fonctions :

* génériques ;
* indépendantes de la logique métier ;
* réutilisables ;
* utiles à plusieurs endroits du programme.

Dans notre projet :

```text
utils.py
   │
   └── clear_screen()
```

Mais un projet plus important pourrait contenir d'autres fonctions utilitaires.

Par exemple :

```python
def clear_screen():
    ...

def pause():
    ...

def format_title(title):
    ...
```

Il faut toutefois éviter de transformer `utils.py` en **« module fourre-tout »**.

Lorsque le nombre de fonctions augmente, il peut être préférable de créer plusieurs modules spécialisés.

---

# ⚠️ 13. Éviter le module « fourre-tout »

Il est important de comprendre que `utils.py` ne doit pas devenir un fichier contenant toutes les fonctions que l'on ne sait pas où placer.

Une bonne question à se poser est :

> **Cette fonction est-elle générique et réutilisable dans plusieurs contextes ?**

Si oui, `utils.py` peut être pertinent.

Si une fonction concerne spécifiquement les participants, elle devrait plutôt être placée dans un module consacré à la gestion des participants.

Par exemple :

```text
❌ utils.py
   supprimer_participant()

✅ gestion_participants.py
   supprimer_participant()
```

En revanche :

```text
✅ utils.py
   clear_screen()
```

est cohérent car l'effacement du terminal n'est pas spécifique aux participants.

---

# 🏗️ 14. `utils.py` dans l'architecture

Les différents refactorings permettent maintenant de construire progressivement une architecture plus claire :

```text
                         ┌──────────────┐
                         │    main.py   │
                         │              │
                         │ orchestration│
                         └──────┬───────┘
                                │
       ┌────────────────────────┼────────────────────────┐
       │                        │                        │
       ▼                        ▼                        ▼
 ┌───────────┐            ┌────────────┐          ┌────────────┐
 │  data.py  │            │data_menu.py│          │  reader.py │
 │           │            │            │          │            │
 │ Données   │            │ Menus      │          │ Saisies    │
 └───────────┘            └────────────┘          └────────────┘
                                                       
                                ┌───────────────────────────┐
                                │         utils.py          │
                                │                           │
                                │   Fonctions utilitaires   │
                                │      clear_screen()       │
                                └───────────────────────────┘
```

Chaque module apporte un service différent.

---

# 📚 15. Les responsabilités des modules

| Module                    | Responsabilité                               |
| ------------------------- | -------------------------------------------- |
| `data.py`                 | Initialiser les données des participants     |
| `data_menu.py`            | Définir les données des menus                |
| `reader.py`               | Lire et valider les saisies utilisateur      |
| `utils.py`                | Fournir des fonctions utilitaires génériques |
| `affichage.py`            | Afficher les informations                    |
| `gestion_participants.py` | Gérer les participants                       |
| `statistiques.py`         | Calculer les statistiques                    |
| `main.py`                 | Orchestrer l'application                     |

On obtient ainsi une séparation progressive des responsabilités.

---

# 🎓 16. Intérêt pédagogique

`utils.py` permet d'introduire une notion importante :

> **Toutes les fonctions d'une application ne sont pas des fonctions métier.**

Certaines fonctions sont simplement **techniques**.

Par exemple :

```text
LOGIQUE MÉTIER
    │
    ├── ajouter un participant
    ├── supprimer un participant
    ├── rechercher un participant
    └── calculer des statistiques

FONCTIONS TECHNIQUES
    │
    ├── effacer l'écran
    ├── gérer une saisie
    └── autres opérations génériques
```

Cette distinction aide l'apprenant à mieux identifier les responsabilités lors d'un refactoring.

---

# 🔄 17. Du code au module réutilisable

La démarche suivie peut être résumée ainsi :

```text
        CODE INITIAL
             │
             ▼
    identifier une tâche
             │
             ▼
       créer une fonction
             │
             ▼
    donner une responsabilité
             │
             ▼
      créer un module
             │
             ▼
      réutiliser ailleurs
```

Dans notre cas :

```text
Effacer l'écran
      ↓
clear_screen()
      ↓
utils.py
      ↓
réutilisable dans d'autres projets
```

---

# 💡 18. Phrase pédagogique à retenir

> 📌 **`utils.py` est un module de fonctions utilitaires génériques. Il encapsule les opérations techniques, comme l'effacement du terminal, afin de les rendre réutilisables par différentes parties de l'application et par d'autres projets.**

---

# 🚀 19. Étape suivante

Nous disposons maintenant de plusieurs modules spécialisés :

```text
data.py
     ↓
Données

data_menu.py
     ↓
Menus

reader.py
     ↓
Saisie

utils.py
     ↓
Outils techniques

affichage.py
     ↓
Présentation

gestion_participants.py
     ↓
Logique métier
```

La prochaine étape consiste à faire communiquer ces différents modules.

Le rôle de `main.py` sera alors de devenir principalement un **orchestrateur** :

```text
                         main.py
                            │
        ┌───────────────────┼───────────────────┐
        ▼                   ▼                   ▼
     data.py          data_menu.py          reader.py
        │                   │                   │
        │                   ▼                   │
        │              affichage.py             │
        │                                       │
        └───────────────┬───────────────────────┘
                        ▼
                logique métier
                        │
                        ▼
                    utils.py
```

L'objectif final est d'avoir un programme dans lequel chaque module **fait une chose précise et la fait correctement**.

---

# 📌 À retenir

```text
                    utils.py
                       │
                       ▼
              clear_screen()
                       │
                       ▼
          ┌─────────────────────┐
          │ Identifier le système│
          └──────────┬──────────┘
                     │
             ┌───────┴───────┐
             ▼               ▼
          Windows       Linux / macOS
             │               │
             ▼               ▼
            cls             clear
```

### Principe fondamental

**Une fonction doit avoir une responsabilité clairement identifiée.**

**Un module doit regrouper des fonctions ayant une cohérence.**

**Une fonction générique peut être réutilisée dans plusieurs contextes.**

`utils.py` illustre donc parfaitement le passage :

```text
REFACTORING
     ↓
IDENTIFICATION D'UNE RESPONSABILITÉ
     ↓
FONCTION clear_screen()
     ↓
MODULE utils.py
     ↓
RÉUTILISABILITÉ
```

C'est une nouvelle étape vers une **application Python modulaire et maintenable**.
