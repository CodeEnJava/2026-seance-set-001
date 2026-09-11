
from data import python, java, web
from data_menu import main_menu, sub_menu
from menu import show_menu
from participants import (add_participant,
                          remove_participant,
                          search_participant,
                          common_participant)
from services import create_group_dict
from statistics import statistics
from display_participants import display_participants
from set_query import query

group_dict = create_group_dict()

while True:
    # menu principal
    choix = show_menu(main_menu)
    # construction du menu en fonction du choix de l'utilisateur
    if choix == 1:
        # Afficher les participants
        print("Afficher les participants")

        while True:
            # le sous menu
            request_choose = show_menu(sub_menu)
            if 1<= request_choose < 5:
                display_participants(request_choose)

            elif request_choose == 5:
                query()
            else:
                input("Retour au menu principal.")
                break

    elif choix == 2:
        # Ajouter un participant
        add_participant()

    elif choix == 3:
        # Supprimer un participant
        remove_participant()

    elif choix == 4:
        # Rechercher un participant
        search_participant()

    elif choix == 5:
        # Participants communs a l'ensemble des activités
        common_participant()

    elif choix == 6:
        # Statistiques
        statistics()

    else:
        print("Vous avez quitté l'application\nA bientôt...")
        break


