from utils import clear_screen
from reader import read_integer_min_max


# Module N°3
# Sa responsabilité l'affichage d'un menu

'''
========================================
       GESTION DES PARTICIPANTS
========================================
'''
def create_title(str_title):
    """
    Affiche un titre encadré par des lignes de caractères '='
    La largeur de l'encadrement est automatiquement adapté à
    la longueur du tire  fourni
    :param str_title: le titre à afficher
    :type str_title: str
    :return: None
    """
    len_title = len(str_title)
    print("="*(14+len_title))
    print(" "*7+str_title)
    print("=" * (14 + len_title))


def create_items(list_items):
    """
    Affiche les items d'un menu sous la forme d'une liste numérotée
    le dernier élément de la liste aura pour indice 0, et va servir
    pour quitter l'application ou la sous application.

    :param list_items: la liste des élemnts à afficher
    :type list_items: list
    :return: None
    """
    choix = 1
    for item in list_items:
        if choix > len(list_items)-1:
            choix = 0

        print(str(choix) + " - " + item)
        choix += 1

def show_menu(dico_menu):
    """
    Affiche un menu et demande à l'utilisateur de sélectionner un choix

    La fonction vérifie d'abord que le dictionnaire fourni correspond
    à la structure attendu d'un menu

    Si le menu est valide, elle :
        * Efface l'écran
        * Affiche le titre du menu
        * Affiche les différents items du menu
        * demande à l'utilisateur de faire un choix
        * elle retourne le choix saisi


    :param dico_menu: un dictionnaire contenant le titre et les differents items du menu
    :type dico_menu : dict
    :return: choix sélectionné par l'utilisateur
    :rtype : int
    :raise TypeError: Si le dictionnaire fourni ne représente pas un menu valide
    """

    # il faut valider le paramètre
    if not is_valide_menu(dico_menu):
       raise TypeError("Le paramètre dico_menu n'est pas un menu valide, "
                       "qui respect le formalisme suivant:\n"
                       "'main_menu = {\'title':une chaine de carctères, "
                       " \n              'items':une liste de str}"

                       )


    # il faut que pour la valeur de la clé items soit une liste

    clear_screen()
    create_title(dico_menu["title"])
    print("\n\n")
    create_items(dico_menu["items"])
    print("\n")
    return read_integer_min_max("Votre choix : ",0,maxi=len(dico_menu["items"]))



def is_valide_menu(dico_menu):
    """
    Vérifie la validité de la structure d'un menu.
    Un menu valide est représenté par un dictionnaire contenant exactement les
    informations nécessaire à son affichage:
        - la cle 'title'  associé à une chaine de caractères
        - la clé 'items' associé à une liste de caractères
    :param dico_menu: dictionnaire représentant le menu à vérifier
    :type dico_menu : dict

    :return: True si le menu est valide, False sinon
    :rtype : bool
    """
    # il faut que le paramètre soit un dictionnaire
    if not isinstance(dico_menu,dict):
        return False

    # il faut que les deux clés soient valides (title et items)
    if "title" not in dico_menu or "items" not in dico_menu:
        return False

    # il faut que pour la valeur de la clé title soit un str
    if not isinstance(dico_menu["title"],str):
        return False

    # il faut que pour la valeur de la clé items soit une liste
    if not isinstance(dico_menu["items"], list):
        return False

    # il faut que chaque éléments de la liste dico_menu["items"] soit un str
    if not is_items_str(dico_menu["items"]):
        return False

    return True


def is_items_str(items):
    """
    Vérifie que tous les items d'une liste sont des chaines de caractères (str)

    La fonction parcourt la liste et retourne False dès qu'un élément n'est pas un str
    si tous les items sont des str retourne True
    :param items: La liste des items à vérifier
    :type items : list
    :return: True si tous les éléments de la liste sont des str, False sinon
    :rtype : bool
    """
    for item in items:
        if not isinstance(item,str):
            return False
    return True




