Voici le `README.md` du module `reader.py`, dans la continuité des README précédents. Il met notamment en évidence le passage de la **saisie directement dans le programme** vers une **fonction réutilisable et spécialisée**.

# ⌨️ `reader.py` — Gérer la saisie utilisateur

## 🎯 Objectif

Le module `reader.py` a une responsabilité clairement définie :

> **Gérer la saisie d'informations provenant de l'utilisateur.**

Dans une démarche de **refactoring** et de **modularité**, l'objectif est de déplacer la gestion des saisies dans un module spécialisé.

Le programme principal ne doit donc plus être responsable de :

* demander directement les saisies ;
* vérifier que l'utilisateur a entré un nombre ;
* contrôler les limites d'une valeur ;
* gérer les erreurs de saisie.

Ces responsabilités sont regroupées dans `reader.py`.

---

# 🧩 1. Le rôle général de `reader.py`

`reader.py` est un **module de lecture des données saisies par l'utilisateur**.

Il fournit des fonctions que les autres modules peuvent appeler lorsqu'ils ont besoin de récupérer une information.

Dans sa première version, le module contient une fonction :

```python
read_integer_min_max(str_message, mini, maxi)
```

Cette fonction permet de demander à l'utilisateur un **nombre entier compris dans un intervalle donné**.

On peut représenter son rôle ainsi :

```text
                 UTILISATEUR
                      │
                      │ saisie
                      ▼
                ┌────────────┐
                │ reader.py  │
                └─────┬──────┘
                      │
                      ▼
             validation de la saisie
                      │
             ┌────────┴────────┐
             │                 │
             ▼                 ▼
          valide             invalide
             │                 │
             ▼                 ▼
        retourne la        redemande
          valeur             une saisie
```

---

# 🔢 2. La fonction `read_integer_min_max()`

La fonction est définie ainsi :

```python
def read_integer_min_max(str_message, mini, maxi):
```

Elle reçoit trois paramètres :

| Paramètre        | Rôle                                  |
| ---------------- | ------------------------------------- |
| `str_message`    | Message affiché à l'utilisateur       |
| `mini`           | Valeur minimale autorisée             |
| `maxi`           | Limite supérieure                     |
| valeur retournée | Entier valide saisi par l'utilisateur |

---

# 🔍 3. Fonctionnement de la saisie

La fonction utilise une boucle :

```python
while True:
```

Cela signifie que la fonction va continuer à demander une valeur **tant qu'une saisie correcte n'a pas été obtenue**.

Le fonctionnement général est :

```text
              Début
                │
                ▼
        demander une valeur
                │
                ▼
        convertir en entier
                │
          ┌─────┴─────┐
          │           │
          ▼           ▼
       succès       erreur
          │           │
          ▼           ▼
   vérifier limite   afficher
          │          message
     ┌────┴────┐        │
     │         │        │
     ▼         ▼        │
   valide   invalide    │
     │         │        │
     ▼         └────────┘
  return
```

---

# 🛡️ 4. Gestion des erreurs avec `try / except`

La conversion de la saisie est réalisée avec :

```python
value = int(input(str_message))
```

Mais l'utilisateur peut saisir autre chose qu'un nombre :

```text
abc
bonjour
12.5
?
```

La conversion en `int` provoquerait alors une erreur `ValueError`.

Pour éviter que le programme s'arrête brutalement, on utilise :

```python
try:
    ...
except ValueError:
    print("Veuillez entrer un nombre valide")
```

Le rôle du `try / except` est donc de **gérer les erreurs de conversion**.

---

# 📏 5. Vérification de l'intervalle

Une fois la valeur convertie en entier, la fonction vérifie qu'elle appartient à l'intervalle demandé :

```python
if value in range(mini, maxi):
    return value
```

Attention :

```python
range(mini, maxi)
```

inclut `mini`, mais **n'inclut pas `maxi`**.

Par exemple :

```python
range(1, 5)
```

produit :

```text
1  2  3  4
```

La valeur `5` n'est donc pas acceptée.

---

# ⚠️ 6. Message en cas de valeur incorrecte

Si la valeur n'est pas comprise dans l'intervalle, la fonction affiche :

```python
print(
    f"Veuillez entrer une valeur comprise entre {mini} et {maxi-1}"
)
```

Puis la boucle `while True` recommence.

L'utilisateur peut donc corriger sa saisie.

---

# 🧠 7. Le code complet

Le module `reader.py` peut être écrit ainsi :

```python
# Module 4
# Sa responsabilité : la saisie d'informations par l'utilisateur

def read_integer_min_max(str_message, mini, maxi):
    while True:
        try:
            value = int(input(str_message))

            if value in range(mini, maxi):
                return value

            print(
                f"Veuillez entrer une valeur comprise "
                f"entre {mini} et {maxi - 1}"
            )

        except ValueError:
            print("Veuillez entrer un nombre valide")
```

---

# 🔄 8. Avant le refactoring

Avant la création de `reader.py`, le programme principal pouvait contenir directement la saisie :

```python
while True:
    try:
        choix = int(input("Votre choix : "))

        if choix in range(1, 8):
            break

        print("Veuillez choisir une valeur comprise entre 1 et 7")

    except ValueError:
        print("Veuillez entrer un nombre valide")
```

Le problème est que cette logique risque d'être **dupliquée** à plusieurs endroits du programme.

Par exemple :

```text
main.py
 │
 ├── saisie du menu principal
 │
 ├── saisie du sous-menu
 │
 ├── saisie d'un choix
 │
 └── saisie d'autres valeurs
```

Le programme principal devient alors responsable de nombreuses opérations.

---

# ✨ 9. Après le refactoring

Avec `reader.py`, cette logique est centralisée dans une fonction :

```python
read_integer_min_max()
```

Le programme qui en a besoin peut simplement l'importer :

```python
from reader import read_integer_min_max
```

Puis l'utiliser :

```python
choix = read_integer_min_max(
    "Votre choix : ",
    1,
    8
)
```

Le code appelant n'a plus besoin de connaître le détail de la validation.

---

# ♻️ 10. Une fonction réutilisable

L'intérêt principal de cette fonction est sa **réutilisabilité**.

La même fonction peut être utilisée pour différents besoins.

### Exemple : menu principal

```python
choix = read_integer_min_max(
    "Votre choix : ",
    1,
    8
)
```

### Exemple : sous-menu

```python
choix = read_integer_min_max(
    "Votre choix : ",
    1,
    7
)
```

### Exemple : sélection d'un participant

```python
numero = read_integer_min_max(
    "Numéro du participant : ",
    1,
    10
)
```

La fonction reste la même.

Seuls ses paramètres changent.

```text
                 read_integer_min_max()
                          │
          ┌───────────────┼───────────────┐
          ▼               ▼               ▼
      menu principal   sous-menu     sélection
```

C'est un excellent exemple de **factorisation du code**.

---

# 🎯 11. Pourquoi utiliser des paramètres ?

La fonction reçoit :

```python
str_message
mini
maxi
```

Cela permet de ne pas écrire une fonction spécifique pour chaque situation.

On pourrait imaginer :

```python
lire_choix_menu_principal()
lire_choix_sous_menu()
lire_numero_participant()
```

Mais cela provoquerait beaucoup de duplication.

Une seule fonction générique suffit :

```python
read_integer_min_max(
    message,
    minimum,
    maximum
)
```

Les paramètres rendent donc la fonction **générique et réutilisable**.

---

# 🧱 12. Une responsabilité unique

`reader.py` ne doit pas prendre en charge toute l'application.

Son rôle est limité à la **lecture et à la validation des informations saisies**.

Il ne doit donc pas :

```text
❌ afficher les menus
❌ gérer les participants
❌ effectuer les statistiques
❌ rechercher un participant
❌ ajouter un participant
❌ supprimer un participant
❌ décider de l'action à effectuer
```

Il doit :

```text
✅ demander une information
✅ convertir la saisie
✅ contrôler sa validité
✅ gérer les erreurs de saisie
✅ retourner une valeur valide
```

---

# 🏛️ 13. `reader.py` dans l'architecture

Après les premiers refactorings, plusieurs responsabilités sont maintenant séparées :

```text
                       APPLICATION
                            │
             ┌──────────────┼──────────────┐
             │              │              │
             ▼              ▼              ▼
         data.py      data_menu.py    reader.py
             │              │              │
             ▼              ▼              ▼
       données des      données des     saisies
       participants       menus        utilisateur
                            │
                            │
                            ▼
                       affichage.py
                            │
                            ▼
                     gestion métier
                            │
                            ▼
                         main.py
```

Chaque module possède ainsi une responsabilité spécifique.

---

# 📚 14. Les responsabilités des modules

| Module                    | Responsabilité                           |
| ------------------------- | ---------------------------------------- |
| `data.py`                 | Initialiser les données des participants |
| `data_menu.py`            | Définir les données des menus            |
| `reader.py`               | Lire et valider les saisies utilisateur  |
| `affichage.py`            | Afficher les informations                |
| `gestion_participants.py` | Gérer les participants                   |
| `statistiques.py`         | Calculer les statistiques                |
| `main.py`                 | Orchestrer l'application                 |

Cette organisation rend l'architecture beaucoup plus lisible.

---

# 🧠 15. Une distinction importante

`reader.py` **ne décide pas quoi faire de la valeur saisie**.

Par exemple :

```python
choix = read_integer_min_max("Votre choix : ", 1, 8)
```

`reader.py` retourne simplement :

```text
1
2
3
...
7
```

C'est un autre module qui décidera ensuite de l'action correspondant au choix.

Par exemple :

```python
if choix == 1:
    ...
elif choix == 2:
    ...
```

Cette distinction est essentielle :

> **`reader.py` lit et valide. Il ne décide pas.**

---

# 🎓 16. Intérêt pédagogique

`reader.py` permet de montrer concrètement le passage :

```text
CODE RÉPÉTÉ
     ↓
IDENTIFICATION D'UNE RESPONSABILITÉ
     ↓
CRÉATION D'UNE FONCTION
     ↓
PARAMÉTRAGE DE LA FONCTION
     ↓
RÉUTILISATION
     ↓
MODULE SPÉCIALISÉ
```

C'est exactement la démarche recherchée dans une séance consacrée au **refactoring et à la modularité**.

L'apprenant comprend qu'une fonction ne sert pas uniquement à raccourcir le code.

Elle permet également de :

* donner un nom à une responsabilité ;
* isoler une logique ;
* réutiliser cette logique ;
* réduire la duplication ;
* rendre le programme principal plus lisible.

---

# 💡 17. Phrase pédagogique à retenir

> 📌 **`reader.py` est un module dédié à la saisie utilisateur : il fournit des fonctions réutilisables permettant de lire et de valider les informations saisies, sans prendre en charge la logique métier de l'application.**

---

# 🚀 18. Étape suivante

La création de `reader.py` permet maintenant de poursuivre la modularisation.

On dispose progressivement de :

```text
data.py
    ↓
Données

data_menu.py
    ↓
Données des menus

reader.py
    ↓
Saisie utilisateur

affichage.py
    ↓
Affichage

gestion_participants.py
    ↓
Logique métier

statistiques.py
    ↓
Calculs

main.py
    ↓
Orchestration
```

L'objectif final est d'obtenir un `main.py` qui ne contient presque plus de détails techniques.

Il doit essentiellement **orchestrer les différentes fonctions et les différents modules**.

---

# 📌 À retenir

```text
                   UTILISATEUR
                        │
                        ▼
                  ┌──────────┐
                  │ reader.py│
                  └────┬─────┘
                       │
                       ▼
              read_integer_min_max()
                       │
              ┌────────┴────────┐
              │                 │
              ▼                 ▼
          saisie valide     saisie invalide
              │                 │
              ▼                 ▼
          return value       nouvelle saisie
```

### Principe fondamental

**Une fonction = une responsabilité.**

**Des paramètres = une fonction réutilisable.**

**Un module = une responsabilité clairement identifiée.**

`reader.py` constitue donc une nouvelle étape importante dans le passage d'un programme monolithique vers une **application Python modulaire**.

Ce module est particulièrement intéressant pédagogiquement, car il permet de faire le lien entre **« j'identifie un bloc de code répétitif » → « j'en fais une fonction » → « je rends la fonction générique avec des paramètres » → « je place cette fonction dans un module spécialisé »**.
