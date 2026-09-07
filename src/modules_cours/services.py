
from data import groupes
from reader import read_integer_min_max
end_with = ": "

def groupe_set():
    dico_groupes ={}
    for pointer in range(0,len(groupes)):
        key = str(pointer+1)
        dico_groupes[key] = groupes[pointer]
    return dico_groupes

def is_items_str(dico_groups):
    if not isinstance(dico_groups,dict):
        raise TypeError("le paramètre doit-être un dictionnaire valide.")
    for key in dico_groups:
        if not isinstance(dico_groups[key], str):
            return False
    return True



def display_groupes(dico_groups):
    '''
    Cette fonction permet d'afficher en console la liste des groupes
    :param dico_groups: le dictionnaire contenant les différents groupes
    :return: None
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
    Cette fonction permet de choisir un groupe
    :param str_message: message pour indiquer l'action
    :param dico_group: dictionnaire contenant le nom des groupes
    :return: un entier indiquant le groupe choisi
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




