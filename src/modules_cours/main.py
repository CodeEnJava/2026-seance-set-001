
from data import python, java, web,groups,group_names
from data_menu import main_menu, sub_menu
from menu import show_menu
from reader import read_str
from services import select_group, create_group_dict
from participants import (add_participant,
                          remove_participant,
                          search_participant,
                          common_participant)


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

            if request_choose == 1:
                print("Les participants du groupe Python")
                for participant in python:
                    print(f" - {participant}")

                input("Retour sous menu ")

            elif request_choose == 2:
                print("Les participants du groupe Java")
                for participant in java:
                    print(f" - {participant}")
                input("Retour sous menu ")

            elif request_choose == 3:
                print("Les participants du groupe Web")
                for participant in web:
                    print(f" - {participant}")
                input("Retour sous menu ")

            elif request_choose == 4:
                print("Les participants de tous les groupes")
                E_union = python.union(java).union(web)
                for participant in E_union:
                    print(f" - {participant}")
                input("Retour sous menu ")

            elif request_choose == 5:
                # Afficher les participants en fonction d'une requête explicite
                print("Vous pouvez utiliser les opérateurs suivants:")
                print(" 1 UNION                : Réunit les éléments des ensembles")
                print(" 2 INTERSECTION         : Éléments communs")
                print(" 3 DIFFERENCE           : Éléments présents dans le premier ensemble uniquement")
                print(" 4 SYMMETRIC_DIFFERENCE : Éléments présents dans un seul des deux ensembles")

                print()
                print("Exemple de requête :\n>> python union java intersection web")
                print()
                prompt = input(">> ")
                # Analyser le contenu du prompt
                prompt = prompt.upper()
                # découper le prompt en n éléments
                elements = prompt.split()
                # pour être valide, on doit avoir au minimum 3 éléments
                if len(elements) <3:
                    print("Requête invalide.")
                else:
                    # il faut vérifier que le premier élément est un ensemble valide
                    valide = False
                    if elements[0]=="PYTHON":
                        result = python.copy()
                    elif elements[0]== "JAVA":
                        result = java.copy()
                    elif elements[0]=="WEB":
                        result = web.copy()
                    else:
                        result = set()
                        print(f"{elements[0]} est un ensemble inconnu.")
                        valide = False
                    if result:
                        valide = True

                    # ENSEMBLE OPERATEUR ENSEMBLE OPERATEUR ENSEMBLE,,,,,,,
                    for i in range(1,len(elements),2):
                        operateur =  elements[i]
                        ensemble = elements[i+1]
                        # identifier l'ensemble
                        if ensemble == "PYTHON":
                            ensemble = python
                        elif ensemble == "JAVA":
                            ensemble = java
                        elif ensemble == "WEB":
                            ensemble = web
                        else:
                            valide = False
                            print(f"{ensemble} est un ensemble inconnu.")
                            break

                        # Appliquer l'opérateur
                        if operateur == "UNION":
                            result = result.union(ensemble)
                        elif operateur == "INTERSECTION":
                            result = result.intersection(ensemble)
                        elif operateur == "DIFFERENCE":
                            result = result.difference(ensemble)
                        elif operateur == "SYMMETRIC_DIFFERENCE":
                            result = result.symmetric_difference(ensemble)
                        else:
                            valide = False
                            print(f"{operateur} est un opérateur inconnu.")
                            break
                    # Afficher le résultat
                    if valide:
                        print("\nRésultat de la requête : ")
                        if result:
                            for participant in result:
                                print(f" - {participant}")
                        else:
                            print("Aucun participant ne correspond à la requête.")
                    else:
                        print(f"{prompt}: cette requête n'est pas valide")

                    input("Retour sous menu ")
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

        print("========================================")
        print("GESTION DES PARTICIPANTS")
        print("========================================\n")

        '''
        Python : 5 participants
        Java   : 4 participants
        Web    : 5 participants
        '''
        print(f"Python : {len(python)} participants")
        print(f"Java   : {len(java)} participants")
        print(f"Web    : {len(web)} participants")

        print()

        print("----------------------------------------")
        print("Participants Python et Java")
        print("----------------------------------------")
        # mise en place d'un ensemble E1, qui contient l'intersection des ensembles
        # python ET java
        E1 = python.intersection(java)
        print(f"Nombre de participant(s) pour python ET java : {len(E1)} ")
        for participant in E1:
            print(f"- {participant}")
        print()
        print("----------------------------------------")
        print("Participants Python et web")
        print("----------------------------------------")
        # mise en place d'un ensemble E2, qui contient l'intersection des ensembles
        # python ET web
        E2 = python.intersection(web)
        print(f"Nombre de participant(s) pour python ET web : {len(E2)} ")
        for participant in E2:
            print(f"- {participant}")
        print()
        print("----------------------------------------")
        print("Participants java et web")
        print("----------------------------------------")
        # mise en place d'un ensemble E3, qui contient l'intersection des ensembles
        # java ET web
        E3 = java.intersection(web)
        print(f"Nombre de participant(s) pour java ET web : {len(E3)} ")
        for participant in E3:
            print(f"- {participant}")

        print()
        print("----------------------------------------")
        print("Participants java et web et python")
        print("----------------------------------------")
        # mise en place d'un ensemble E4, qui contient l'intersection des ensembles
        # (python ET web) ET java
        E4 = (python.intersection(web)).intersection(java)
        print(f"Nombre de participant(s) pour  python ET web ET java: {len(E4)} ")
        for participant in E4:
            print(f"- {participant}")

        input("Retour au menu principal")
    else:
        print("Vous avez quitté l'application\nA bientôt...")
        break


