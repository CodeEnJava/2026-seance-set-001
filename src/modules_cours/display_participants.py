from data import group_names,groups

def display_set_participants(group):
    """
    Affiche les participants contenus dans un ensemble

    La fonction parcourt l'ensemble fourni en paramètre et affiche
    chaque participant sur une ligne dans la console.

    :param group: Ensemble contenant les participants à afficher
    :type group: set
    :return: Aucun retour
    :rtype: None
    """
    for participant in group:
        print(f" - {participant}")

def display_participants(index):
    """
    Affiche les participants correspondant au groupe sélectionné.

    La fonction utilise l'indice (index) fourni pour identifier le groupe
    dont les participants doivent être affichés

    Si l'indice correspond à un groupe existant, les participants de ce groupe
    sont affiché.

    Si l'indice vaut 4, la fonction affiche l'ensemble des participants de tous
    les groupes.

    Si l'indice ne correspond à aucune option valide, un message d'erreur est envoyé dans
    la console

    :param index: Le numéro correspondant au groupe sélectionné OU à l'option
                  permettant d'afficher tous les participants.
    :type index: int
    :return: Aucune information. Les informations sont affichés dans la console.
    :rtype: None
    """
    if (index-1) in range(0,len(group_names)):
        print(f"Les participants du groupe {group_names[index-1].capitalize()}")
        display_set_participants(groups[group_names[index-1].lower()])
    elif index ==4:
        all_participants = get_all_participants()
        print("Les participants de tous les groupes")
        display_set_participants(all_participants)

    input("Retour sous menu ")

def get_all_participants():
    """
    Récupère l'ensemble des participants présents dans tous les groupes.

    La fonction réalise l'union des ensembles participants associés aux
    différents groupes définis dans le module data.py

    :return: Ensemble contenant tous les participants des différents groupes
    :rtype:set
    """
    # initialiser le premier ensemble
    participants = groups[group_names[0].lower()]

    # Union progressive avec les autres ensembles
    for pointer in range(1,len(group_names)):
        group = groups[group_names[pointer].lower()]
        participants = participants.union(group)

    return participants
