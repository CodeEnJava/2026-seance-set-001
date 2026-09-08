
from data import group_names
from reader import read_integer_min_max
end_with = ": "

def create_group_dict():
    '''
       Crée un dictionnaire associant un numéro de groupe à son nom.

       La fonction parcourt la collection globale `groupes` et construit
       un dictionnaire dont :

       - la clé correspond au numéro du groupe sous forme de chaîne de caractères ;
       - la valeur correspond au nom du groupe.

       La numérotation des groupes commence à 1 afin de faciliter
       leur affichage et leur sélection par l'utilisateur.

       :return: un dictionnaire contenant les numéros et les noms des groupes
       :rtype: dict
       '''
    dico_groupes ={}
    for pointer in range(0,len(group_names)):
        key = str(pointer+1)
        dico_groupes[key] = group_names[pointer]
    return dico_groupes

def is_items_str(dico_groups):
    '''
       Vérifie que toutes les valeurs d'un dictionnaire sont des chaînes
       de caractères.

       La fonction commence par vérifier que le paramètre fourni est bien
       un dictionnaire. Si ce n'est pas le cas, une exception TypeError
       est levée.

       Ensuite, chaque valeur du dictionnaire est contrôlée afin de vérifier
       qu'elle est de type str.

       :param dico_groups: dictionnaire contenant les éléments à vérifier
       :type dico_groups: dict

       :return: True si toutes les valeurs sont des chaînes de caractères,
                False si au moins une valeur n'est pas une chaîne
       :rtype: bool

       :raises TypeError: si le paramètre fourni n'est pas un dictionnaire
       '''
    if not isinstance(dico_groups,dict):
        raise TypeError("le paramètre doit-être un dictionnaire valide.")
    for key in dico_groups:
        if not isinstance(dico_groups[key], str):
            return False
    return True



def display_groupes(dico_groups):
    '''

    :param dico_groups:
    :return:
    '''
    if not isinstance(dico_groups,dict):
        raise TypeError("le paramètre doit-être un dictionnaire valide.")
    # il faut s'assurer que chaque item du dictionnaire est un str
    if not is_items_str(dico_groups):
        raise TypeError("Le dictionnaire n'est pas valide, "
                        "il faut que les items soit des str.")

    for key, value in dico_groups.items():
        print(f" {key} - {value.capitalize()}")

def select_group(str_message,dico_group):
    '''

    :param str_message: message pour indiquer l'action
    :param dico_group: dictionnaire contenant le nom des groupes
    :return: un entier indiquant le groupe choisi
    :rtype : int
    '''
    # validation des paramètres
    if not isinstance(str_message,str):
        raise TypeError("Le premier paramètre doit-être un str.")

    if not isinstance(dico_group, dict):
        raise TypeError("Le second paramètre doit-être un dictionnaire valide.")

    if not is_items_str(dico_group):
        raise TypeError("Le dictionnaire n'est pas valide, "
                        "il faut que les items soit des str.")
    if len(str_message) == 0:
        message = "Choisir un groupe"
    else:
        message = str_message
    if not message.endswith(end_with):
        message = message +end_with

    message = message.capitalize()
    print(message+"\n")
    display_groupes(dico_group)
    print()
    return read_integer_min_max("Votre choix de groupe : ",1,len(dico_group)+1)




