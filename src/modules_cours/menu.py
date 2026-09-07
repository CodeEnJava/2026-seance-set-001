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
    len_title = len(str_title)
    print("="*(14+len_title))
    print(" "*7+str_title)
    print("=" * (14 + len_title))


def create_items(list_items):
    choix = 1
    for item in list_items:
        if choix > len(list_items)-1:
            choix = 0

        print(str(choix) + " - " + item)
        choix += 1

def show_menu(list_menu):
    # validation du paramètre

    clear_screen()
    create_title(list_menu["title"])
    print("\n\n")
    create_items(list_menu["items"])
    print("\n")
    return read_integer_min_max("Votre choix : ",0,maxi=len(list_menu["items"]))








