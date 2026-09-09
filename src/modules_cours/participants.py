# Module participants
# Sa responsabilité:
# * Gérer les opérations effectuées sur les participants des différents groupes de formation.
#       -> add_participant()
#       -> remove_participant()
#       -> search_participant()
#       -> common_participant()
# ici on va être sur une logique métier

from data import group_names,groups
from reader import read_str
from services import select_group,create_group_dict


group_dict = create_group_dict()

def add_participant_aux(name, pointer_group):
    """
       Ajoute un participant dans le groupe de formation sélectionné.

       Cette fonction réalise l'opération métier d'ajout d'un participant.
       Le groupe est identifié à partir de son numéro, puis le nom du
       participant est ajouté à l'ensemble correspondant.

       Parameters
       ----------
       name : str
           Nom du participant à ajouter.

       pointer_group : int
           Numéro du groupe dans lequel le participant doit être ajouté.
           La numérotation des groupes commence à 1.

       Returns
       -------
       None
           Cette fonction ne retourne aucune valeur.

       Notes
       -----
       Les participants sont stockés dans des ensembles (`set`). Par
       conséquent, si le participant est déjà présent dans le groupe,
       son nom ne sera pas ajouté une seconde fois.
       """
    groups[group_names[pointer_group-1].lower()].add(name)
    group = group_names[pointer_group-1].lower()
    print(f"{name} a été ajouté au groupe {group}")

def add_participant():
    """
    Gère l'ajout interactif d'un nouveau participant dans un groupe.

    Cette fonction constitue la partie interactive de l'opération
    d'ajout d'un participant. Elle :

    - affiche un message indiquant l'opération en cours ;
    - demande à l'utilisateur le nom du nouveau participant ;
    - demande dans quel groupe le participant doit être ajouté ;
    - appelle `add_participant_aux()` afin de réaliser l'ajout ;
    - attend une action de l'utilisateur avant le retour au menu principal.

    Returns
    -------
    None
        Cette fonction ne retourne aucune valeur.

    Notes
    -----
    La saisie du nom est réalisée à l'aide de la fonction `read_str()`.
    La sélection du groupe est réalisée à l'aide de la fonction
    `select_group()`.

    L'ajout effectif du participant dans la structure de données est
    délégué à la fonction `add_participant_aux()`.
    """

    print("Ajouter un participant")
    nom = read_str("Entrer le nom du nouveau participant")

    groupe = select_group("Dans quel groupe voulez-vous l'ajouter ? ", group_dict)

    add_participant_aux(nom, groupe)

    input("Retour au menu principal")



def remove_participant_aux(name, pointer_group):
    """
    Supprime un participant du groupe de formation sélectionné.

    Cette fonction réalise l'opération métier de suppression d'un participant.
    Le groupe est identifié à partir de son numéro, puis le nom du participant
    est recherché dans l'ensemble correspondant.

    Si le participant est présent dans le groupe, il est supprimé de
    l'ensemble. Dans le cas contraire, un message informe l'utilisateur
    que le participant n'appartient pas au groupe sélectionné.

    Parameters
    ----------
    name : str
        Nom du participant à supprimer.

    pointer_group : int
        Numéro du groupe dans lequel le participant doit être supprimé.
        La numérotation des groupes commence à 1.

    Returns
    -------
    None
        Cette fonction ne retourne aucune valeur.

    Notes
    -----
    Les participants sont stockés dans des ensembles (`set`). La suppression
    est donc précédée d'une vérification afin de s'assurer que le participant
    est bien présent dans le groupe avant d'utiliser la méthode `remove()`.
    """
    if name in groups[group_names[pointer_group - 1].lower()]:
        # suppression
        groups[group_names[pointer_group - 1].lower()].remove(name)
        print(f"{name} a été supprimée du groupe {group_names[pointer_group - 1].capitalize()}")
    else:
        print(f"{name} n'est pas dans le groupe {group_names[pointer_group - 1].capitalize()}")

def remove_participant():
    """
    Gère la suppression interactive d'un participant d'un groupe.

    Cette fonction constitue la partie interactive de l'opération de
    suppression d'un participant. Elle :

    - affiche un message indiquant l'opération en cours ;
    - demande à l'utilisateur le nom du participant à supprimer ;
    - demande dans quel groupe le participant doit être supprimé ;
    - appelle `remove_participant_aux()` afin de réaliser la suppression ;
    - attend une action de l'utilisateur avant le retour au menu principal.

    Returns
    -------
    None
        Cette fonction ne retourne aucune valeur.

    Notes
    -----
    La saisie du nom du participant est réalisée à l'aide de la fonction
    `read_str()`.

    La sélection du groupe est réalisée à l'aide de la fonction
    `select_group()`.

    La suppression effective du participant est déléguée à la fonction
    `remove_participant_aux()`, qui contient la logique métier associée
    à cette opération.
    """
    print("Supprimer un participant")

    name = read_str("Entrer le nom du participant à supprimer")

    groupe = select_group("Dans quel groupe voulez-vous le supprimer ? ", group_dict)

    remove_participant_aux(name, groupe)

    input("Retour au menu principal")


def search_participant_aux(name):
    """
    Recherche un participant dans l'ensemble des groupes et affiche sa présence

    Parcourt l'ensemble des groupes qui sont enregistrés dans le module data.py,
    pour identifier ceux auxquels appartient le participant spécifié dans le paramètre,
    puis afficher le résultat dans la console (absence, un groupe unique, groupes multiples)/

    :param name: Le nom du participant à rechercher
    :type name: str
    :return: Aucune valeur, les résultats sont directement affichés en console
    :rtype: None
    """

    # il faut rechercher un participant et indiquer dans quel groupe il appartient
    # Il peut aussi appartenir à plusieurs groupe

    prefixe = ", "
    str_group = ""
    str_group_filter = ""

    for group in group_names:
        # group représente la cle du dictionnaire groups
        # groups[group] --> retourne un ensemble, il suffira de vérifier si name fait parti de l'ensemble
        if name in groups[group.lower()]:
            str_group += prefixe+group.capitalize()
            str_group_filter = str_group.removeprefix(prefixe)

    if str_group_filter.count(prefixe) > 0:
        print(f"{name} est présent dans les groupes : {str_group_filter}")
    elif str_group_filter.count(prefixe) == 0 and len(str_group_filter) > 0:
        print(f"{name} est dans le groupe {str_group_filter}")
    else:
        print(f"{name} n'est dans aucun groupe")

def search_participant():
    """
    Interagit avec l'utilisateur pour lancer la recherche d'un participant.
    1- Demande la saisie du nom du participant
    2- Exécute la recherche en utilisant la fonction search_participant_aux()
    3- Afffiche le resultta de la recherche
    4- Attend la validation de l'utilisateur pour retourner au programme principal
    :return: Aucune valeur
    :rtype: None
    """
    print("Rechercher un participant")

    name = read_str("Entrer le nom du participant à rechercher : ")

    # Rechercher s'il est présent dans l'ensemble python
    search_participant_aux(name)

    input("Retour au menu principal")


