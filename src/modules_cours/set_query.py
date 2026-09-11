from data import groups, group_names
from display_participants import display_set_participants

def display_query_help():
    """

    :return:
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

    :param set_name:
    :return:
    """
    if not set_name in group_names:
        return None
    return groups[set_name.lower()]

def execute_query(prompt):
    """

    :param prompt:
    :return:
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

    :return:
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





