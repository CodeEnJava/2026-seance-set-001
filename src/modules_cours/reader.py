
# Module 4
# Sa responsabilité : la saisie d'informations par l'utilisateur

end_with = ": "


def read_integer_min_max(str_message,mini,maxi):
    '''
    cette fonction permet de lire un entier dont la valeur doit appartenir
    aux bornes définies par mini et maxi tel que 'n' appartiert [mini,maxi[
    :param str_message: message explicatif sur la demande de la saisie
    :param mini: la valeur mini acceptée
    :param maxi: la valeur maxi acceptée
    :return: la valeur entière lue au clavier
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
    Cette fonction permet de lire une chaine de caractères non null au clavier
    :param str_message: message explicatif sur la demande de la saisie
    :return: la chaine de caractères lue au clavier
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


