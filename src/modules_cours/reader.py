'''
Rôle du module reader.py

Le module reader.py est responsable de la saisie et de la validation des informations entrées
par l’utilisateur au clavier.

Il centralise les fonctions permettant de demander différentes valeurs à l’utilisateur tout
en contrôlant leur validité.

Dans cette version, le module propose notamment deux fonctions :

    *   read_integer_min_max() : lit un entier et vérifie qu’il appartient à un intervalle donné ;
    *   read_str() : lit une chaîne de caractères non vide et la formate automatiquement.

L’objectif est d'éviter de dupliquer dans les différents modules de l’application
le code de saisie et de contrôle des données.
Le module reader.py constitue donc une couche dédiée aux entrées utilisateur.

Exemple d'utilisation
Supposons que le programme principal doive demander à l'utilisateur son nom puis choisir
une option dans un menu.

from reader import read_str, read_integer_min_max

# Saisie du nom
name = read_str("Entrer votre nom")

# Saisie d'une option comprise entre 1 et 5
choice = read_integer_min_max("Choisir une option", 1, 6)

print(f"Bonjour {name} !")
print(f"Vous avez choisi l'option {choice}.")

L'utilisateur peut obtenir :

Entrer votre nom : alice
Choisir une option : 3

Bonjour Alice !
Vous avez choisi l'option 3.
Exemple avec une saisie incorrecte

Si l'utilisateur saisit :
Choisir une option : abc

la fonction affiche :
Veuillez entrer un nombre valide
et redemande automatiquement une saisie.

Si l'utilisateur saisit :
Choisir une option : 8
la fonction affiche :

Veuillez entrer une valeur comprise entre 1 et 5
et redemande une nouvelle valeur.

Intérêt dans la modularité
Sans ce module, chaque partie de l'application devrait gérer elle-même les saisies.
Avec reader.py, cette logique est centralisée et réutilisable.

Le programme appelant n'a donc plus besoin de connaître les détails de la validation.

Principe de modularité : chaque module possède une responsabilité clairement définie.
Ici, reader.py s'occupe de lire et valider les données saisies par l'utilisateur,
tandis que les autres modules peuvent se concentrer sur leur propre responsabilité.

| Élément                  | Rôle                                            |
| ------------------------ | ----------------------------------------------- |
| `reader.py`              | Gérer les saisies utilisateur                   |
| `read_str()`             | Lire et valider une chaîne non vide             |
| `read_integer_min_max()` | Lire et valider un entier dans un intervalle    |
| `end_with`               | Garantir une présentation homogène des messages |
| `TypeError`              | Contrôler les paramètres des fonctions          |
| `ValueError`             | Gérer une saisie entière invalide               |

En résumé :
reader.py permet de centraliser, sécuriser et réutiliser la logique de saisie utilisateur,
ce qui contribue directement à rendre l'application plus modulaire et plus facile à maintenir.
'''

end_with = ": "


def read_integer_min_max(str_message,mini,maxi):
    '''
         Lit et retourne un nombre entier saisi au clavier.

        La valeur saisie doit respecter l'intervalle [mini, maxi[ :
            mini <= valeur < maxi

        La fonction contrôle les paramètres reçus, demande à l'utilisateur
        de saisir une valeur jusqu'à obtenir un entier valide appartenant
        à l'intervalle demandé.

        :param str_message: message affiché pour demander la saisie
        :param mini: borne minimale incluse dans l'intervalle
        :param maxi: borne maximale exclue de l'intervalle
        :return: entier saisi et validé par la fonction
        :raises TypeError: si les paramètres ne sont pas du type attendu
    '''

    # vérifier si le paramètre str_message est bien une instance de la classe str
    if not isinstance(str_message, str):
        raise TypeError("Le paramètre doit-être une chaine de caractères.")

    # vérifier si mini et maxi sont des nombres entiers
    if not isinstance(mini, int):
        raise TypeError("Le paramètre doit-être un nombre entier.")
    if not isinstance(maxi, int):
        raise TypeError("Le paramètre doit-être un nombre entier.")

    # il faut avoir mini< maxi
    if mini >= maxi :
        raise TypeError("Il faut avoir mini<maxi :")

    if len(str_message) == 0:
        message = "Entrer une valeur entière"
    else:
        message = str_message

    # on souhaite savoir si la fin du message est ': '
    if not message.endswith(end_with):
        message = message + end_with

    while True:
        try:
            value = int(input(message))
            if value in range(mini, maxi):
                return value
            print(f"Veuillez entrer une valeur comprise entre {mini} et {maxi-1}")
        except ValueError:
            print("Veuillez entrer un nombre valide")


def read_str(str_message):
    '''
        La fonction read_str() permet de lire une chaîne de caractères saisie par l’utilisateur au clavier.
        Elle garantit que :
            + le message fourni en paramètre est bien une chaîne de caractères ;
            + le message affiché à l’utilisateur est correctement formaté avec ": " ;
            + la saisie n’est pas vide ;
            + la première lettre de la chaîne saisie est automatiquement mise en majuscule ;

        la fonction redemande une saisie tant que l’utilisateur ne fournit pas une chaîne non vide.

        Utilisation

        La fonction reçoit en paramètre un message destiné à expliquer à l’utilisateur ce qu’il doit saisir.
        name = read_str("Entrer votre nom")

        La fonction affiche alors :

            Entrer votre nom :

        L’utilisateur saisit par exemple :

            alice

        La fonction retourne :

            "Alice"
    Valeur retournée

    La fonction retourne la chaîne de caractères saisie par l’utilisateur, après avoir appliqué capitalize().
    Si l’utilisateur saisit une chaîne vide, la fonction affiche :
    Entrer une chaine non vide
    et demande une nouvelle saisie.

    Gestion des erreurs

    Si le paramètre str_message n’est pas une chaîne de caractères,
    la fonction déclenche une exception TypeError.

    Exemple :

    read_str(123)
    provoque :
    TypeError: Le paramètre doit-être une chaine de caractères.

    Synthèse:
    read_str() centralise donc la saisie sécurisée d’une chaîne de caractères non vide.

    Elle permet d'éviter de répéter dans le programme la logique de contrôle suivante :
    while True:
        name = input(...)
        if len(name) != 0:
        ...
        break

    Cette fonction participe ainsi à la modularité de l’application en regroupant dans
    une seule fonction la responsabilité de la saisie et de sa validation.

    :param str_message:message indiquant à l'utilisateur l'action ou
                       l'instruction à réaliser
    :return:une chaine de caractères non vide saisie par l'utilisateur
    '''

    # vérifier si le paramètre str_message est bien une instance de la classe str
    if not isinstance(str_message, str):
        raise TypeError("Le paramètre doit-être une chaine de caractères.")

    if len(str_message) == 0:
        message ="Entrer une chaine non vide"
    else:
        message = str_message

    # on souhaite savoir si la fin du message est ': '
    if not message.endswith(end_with):
        message = message+end_with

    while True:
        name = input(message)
        if len(name) != 0:
            name = name.capitalize()
            return name
        print("Entrer une chaine non vide")


