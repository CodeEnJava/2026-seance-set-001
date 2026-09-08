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