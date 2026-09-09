
from menu import create_title
from modules_cours.data import groups, group_names
from participants import common_participant_aux


def display_group_sizes():
    """
       Affiche le nombre de participants pour chaque groupe.

       La fonction parcourt le dictionnaire `groups` et affiche,
       pour chaque groupe, son nom ainsi que le nombre de participants.

       :return: Aucune valeur. Les informations sont affichées dans la console.
       :rtype: None
    """
    for group_name, participants in groups.items():
        print(f"{group_name.capitalize():<10} : {len(participants)} participants")

def intersection_sets_aux(pointer_group_a, pointer_group_b):
    """
       Calcule l'intersection de deux groupes de participants.

       La fonction récupère les ensembles de participants correspondant
       aux deux groupes identifiés par leurs pointeurs, puis calcule
       l'ensemble des participants communs aux deux groupes.

       Cette fonction réalise uniquement le traitement métier et ne
       gère aucun affichage ni contrôle des paramètres.

       :param pointer_group_a: Indice du premier groupe dans `group_names`.
       :type pointer_group_a: int
       :param pointer_group_b: Indice du second groupe dans `group_names`.
       :type pointer_group_b: int
       :return: Ensemble contenant les participants communs aux deux groupes.
       :rtype: set
    """
    set_a = groups[group_names[pointer_group_a].lower()]
    set_b = groups[group_names[pointer_group_b].lower()]

    return set_a.intersection(set_b)

def intersection_sets(pointer_group_a, pointer_group_b):
    """
        Affiche les participants communs à deux groupes.

        La fonction vérifie la validité des deux pointeurs, récupère
        les noms des groupes concernés, puis appelle
        `intersection_sets_aux()` pour calculer leur intersection.

        Elle affiche ensuite le titre, le nombre de participants communs
        ainsi que la liste des participants concernés.

        Les deux pointeurs doivent :

        - être des entiers ;
        - correspondre à des indices valides de `group_names` ;
        - être différents.

        :param pointer_group_a: Indice du premier groupe dans `group_names`.
        :type pointer_group_a: int
        :param pointer_group_b: Indice du second groupe dans `group_names`.
        :type pointer_group_b: int
        :return: Aucune valeur. Le résultat est affiché dans la console.
        :rtype: None
        :raises TypeError: Si l'un des paramètres n'est pas un entier.
        :raises ValueError: Si les deux pointeurs sont identiques.
        :raises ValueError: Si l'un des pointeurs est en dehors des limites
                           de `group_names`.
    """

    if not isinstance(pointer_group_a,int):
        raise TypeError("Le premier paramètre doit-être un entier.")
    if not isinstance(pointer_group_b,int):
        raise TypeError("Le second paramètre doit-être un entier.")

    if pointer_group_a == pointer_group_b:
        raise ValueError("Les deux pointeurs ne peuvent pas être identiques.")

    if not 0 <= pointer_group_a < len(group_names) or not 0 <= pointer_group_b < len(group_names):
        raise ValueError("La valeur se trouve en dehors des limites.")

    print()

    group_name_a = group_names[pointer_group_a].capitalize()
    group_name_b = group_names[pointer_group_b].capitalize()

    common_participants = intersection_sets_aux(pointer_group_a,pointer_group_b)

    create_title(f"Participants {group_name_a} et {group_name_b}")

    print(f"Nombre de participant(s) pour {group_name_a} ET {group_name_b} : {len(common_participants)} ")
    print()
    for participant in common_participants:
        print(f"- {participant}")


def common_intersection_sets():
    """
        Affiche les participants communs à l'ensemble des groupes.

        La fonction appelle `common_participant_aux()` afin de récupérer
        l'ensemble des participants présents dans tous les groupes.

        Les noms des groupes sont ensuite récupérés et assemblés afin
        de construire dynamiquement le titre et les informations affichées.
        Cette approche permet à la fonction de fonctionner quel que soit
        le nombre de groupes enregistrés dans `group_names`.

        La fonction affiche ensuite le titre, le nombre de participants
        communs ainsi que la liste des participants concernés.

        :return: Aucune valeur. Le résultat est affiché dans la console.
        :rtype: None
    """
    common_participants = common_participant_aux()

    list_names =[]
    for group_name in group_names:
        list_names.append(group_name.capitalize())

    # java, web, python, html et sql
    str_group_name = list_names[0]

    for index in range(1,len(list_names)-1):
        str_group_name += ", "+list_names[index]

    str_group_name += " et " + list_names[-1]

    create_title(f"Participants {str_group_name}")

    print(f"Nombre de participant(s) pour  {str_group_name}: {len(common_participants)} ")

    for participant in common_participants:
        print(f"- {participant}")



def statistics():
    """
           Affiche les statistiques relatives aux participants.

           La fonction présente successivement :

           - le nombre de participants dans chaque groupe ;
           - les participants communs aux groupes Python et Java ;
           - les participants communs aux groupes Java et Web ;
           - les participants communs aux groupes Web et Python ;
           - les participants communs à l'ensemble des groupes.

           La fonction attend ensuite une saisie de l'utilisateur avant
           de permettre le retour au menu principal.

           :return: Aucune valeur. Les statistiques sont affichées dans la console.
           :rtype: None
    """
    create_title("GESTION DES PARTICIPANTS")
    print()
    display_group_sizes()

    intersection_sets(0,1)

    intersection_sets(1,2)

    intersection_sets(2,0)

    common_intersection_sets()
    print()
    input("Retour au menu principal")

