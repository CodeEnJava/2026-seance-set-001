from data import groups, group_names
from display_participants import display_set_participants

def display_query_help():
    """
        Affiche l'aide permettant à l'utilisateur de connaître les opérateurs
        disponibles pour effectuer des requêtes sur les ensembles de participants.

        Les opérateurs disponibles sont :
            - UNION
            - INTERSECTION
            - DIFFERENCE
            - SYMMETRIC_DIFFERENCE

        Un exemple de syntaxe de requête est également affiché.

        :return: Aucun retour.
        :rtype: None
    """
    print("Vous pouvez utiliser les opérateurs suivants:")
    print(" 1 UNION                : Réunit les éléments des ensembles")
    print(" 2 INTERSECTION         : Éléments communs")
    print(" 3 DIFFERENCE           : Éléments présents dans le premier ensemble uniquement")
    print(" 4 SYMMETRIC_DIFFERENCE : Éléments présents dans un seul des deux ensembles")

    print()
    print("Exemple de requête :\n>> python union java intersection web")
    print()

def get_set(set_name):
    """
        Recherche et retourne l'ensemble de participants correspondant au nom
        d'un groupe.

        Le nom fourni est vérifié dans la collection des noms de groupes.
        Si le groupe existe, l'ensemble de participants associé est retourné.
        Dans le cas contraire, la fonction retourne None.

        :param set_name: Nom du groupe dont l'ensemble de participants doit être récupéré.
        :type set_name: str
        :return: L'ensemble de participants du groupe ou None si le groupe est inconnu.
        :rtype: set ou None
    """
    if not set_name in group_names:
        return None
    return groups[set_name.lower()]

def execute_query(prompt):
    """
        Analyse et exécute une requête permettant d'effectuer des opérations
        entre plusieurs ensembles de participants.

        La requête doit respecter la syntaxe suivante :

            ENSEMBLE OPERATEUR ENSEMBLE
            ENSEMBLE OPERATEUR ENSEMBLE OPERATEUR ENSEMBLE
            ...

        Les opérateurs disponibles sont :
            - UNION
            - INTERSECTION
            - DIFFERENCE
            - SYMMETRIC_DIFFERENCE

        Les opérations sont exécutées de gauche à droite.

        :param prompt: Requête saisie par l'utilisateur.
        :type prompt: str
        :return: Ensemble résultant de l'exécution de la requête.
        :rtype: set
        :raises ValueError: Si la syntaxe de la requête est invalide, si un ensemble
                            est inconnu ou si un opérateur n'est pas reconnu.
    """
    # Analyser le contenu du prompt
    prompt = prompt.upper()
    # découper le prompt en n éléments
    elements = prompt.split()
    # pour être valide, on doit avoir au minimum 3 éléments
    if len(elements) < 3 or len(elements)%2 == 0:
        raise ValueError("Requête n'est pas valide.")

    result = get_set(elements[0])

    if result is None:
        raise ValueError(f"{elements[0]} est un ensemble inconnu.")

    result = result.copy()

    # ENSEMBLE OPERATEUR ENSEMBLE OPERATEUR ENSEMBLE,,,,,,,
    for i in range(1, len(elements), 2):
        operator = elements[i]
        set_name = elements[i + 1]

        current_set = get_set(set_name)

        if current_set is None:
            raise ValueError(f"{set_name} est un ensemble inconnu.")

        # Appliquer l'opérateur
        if operator == "UNION":
            result = result.union(current_set)
        elif operator == "INTERSECTION":
            result = result.intersection(current_set)
        elif operator == "DIFFERENCE":
            result = result.difference(current_set)
        elif operator == "SYMMETRIC_DIFFERENCE":
            result = result.symmetric_difference(current_set)
        else:
            raise ValueError(f"{operator} est un opérateur inconnu.")
    return result

def query():
    """
        Permet à l'utilisateur de saisir et d'exécuter une requête sur les
        ensembles de participants.

        La fonction affiche d'abord l'aide relative aux opérateurs disponibles,
        récupère la requête saisie par l'utilisateur, puis exécute cette requête.

        Si la requête est valide, les participants correspondant au résultat sont
        affichés. Si aucun participant ne correspond à la requête, un message
        approprié est affiché.

        Les erreurs liées à une requête invalide, à un ensemble inconnu ou à un
        opérateur inconnu sont interceptées et affichées à l'utilisateur.

        :return: Aucun retour.
        :rtype: None
    """
    display_query_help()
    prompt = input(">> ")

    try:
        result = execute_query(prompt)
        print("\nRésultat de la requête : ")
        if result:
            display_set_participants(result)
        else:
            print(f"Aucun participant ne correspond à la requête:\n{prompt.lower()}")
    except ValueError as error:
        print(f"Erreur :{error}")

    input("Retour sous menu ")





