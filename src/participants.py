import subprocess
import platform


# Initialisation des 3 ensembles
python = {
    "Alice",
    "Bob",
    "Charlie",
    "David",
    "Emma"
}

java = {
    "Bob",
    "David",
    "Franck",
    "Emma"
}

web = {
    "Alice",
    "Charlie",
    "Emma",
    "Franck",
    "Gérard"
}

# mise en place du menu
'''
========================================
       GESTION DES PARTICIPANTS
========================================

1 - Afficher les participants
2 - Ajouter un participant
3 - Supprimer un participant
4 - Rechercher un participant
5 - Participants communs
6 - Statistiques
0 - Quitter

Votre choix :

modification par rapport au cahier des charges :

=============================================================
       Requête d'affichage des participants
=============================================================


1 - Afficher les participants du groupe Python
2 - Afficher les participants du groupe Java
3 - Afficher les participants du groupe Web
4 - Afficher les participants de tous les groupes
5 - Afficher les participants en fonction d'une requête
0 - Retour au menu principal

Votre choix : 

'''

while True:
    '''
    Effacer écran
    '''
    if platform.system() == "Windows":
        subprocess.run("cls",shell= True)
    else:
        subprocess.run("clear", shell = True)

    print("\n========================================")
    print("       GESTION DES PARTICIPANTS")
    print("========================================\n")
    print("1 - Afficher les participants")
    print("2 - Ajouter un participant")
    print("3 - Supprimer un participant")
    print("4 - Rechercher un participant")
    print("5 - Participants communs")
    print("6 - Statistiques")
    print("0 - Quitter\n")

    # Lecture sécurisée du choix
    while True:
        try:
            choix = int(input("Votre choix :" ))
            if choix in range(0,7):
                break
            print("Veuillez entrer une valeur comprise entre 0 et 6")
        except ValueError:
            print("Veuillez entrer un nombre valide")
    # fin de la lecture sécurisée

    # construction du menu en fonction du choix de l'utilisateur

    if choix == 1:
        # Afficher les participants
        # TODO : dans la prochaine vidéo réalisation du code
        print("Afficher les participants")

        while True:
            '''
               Effacer écran
               '''
            if platform.system() == "Windows":
                subprocess.run("cls", shell=True)
            else:
                subprocess.run("clear", shell=True)

            print("=============================================================")
            print("Requête d'affichage des participants")
            print("=============================================================\n")


            print("1 - Afficher les participants du groupe Python")
            print("2 - Afficher les participants du groupe Java")
            print("3 - Afficher les participants du groupe Web")
            print("4 - Afficher les participants de tous les groupes")
            print("5 - Afficher les participants en fonction d'une requête")
            print("0 - Retour au menu principal")
            print("\n")
            # Lecture sécurisée du choix
            while True:
                try:
                    reqchoix = int(input("Votre choix :"))
                    if reqchoix in range(0, 6):
                        break
                    print("Veuillez entrer une valeur comprise entre 0 et 5")
                except ValueError:
                    print("Veuillez entrer un nombre valide")
            # fin de la lecture sécurisée

            if reqchoix == 1:
                print("Les participants du groupe Python")
                for participant in python:
                    print(f" - {participant}")

                input("Retour sous menu ")

            elif reqchoix == 2:
                print("Les participants du groupe Java")
                for participant in java:
                    print(f" - {participant}")
                input("Retour sous menu ")

            elif reqchoix == 3:
                print("Les participants du groupe Web")
                for participant in web:
                    print(f" - {participant}")
                input("Retour sous menu ")

            elif reqchoix == 4:
                print("Les participants de tous les groupes")
                E_union = python.union(java).union(web)
                for participant in E_union:
                    print(f" - {participant}")
                input("Retour sous menu ")

            elif reqchoix == 5:
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
        print("Ajouter un participant")
        # saisir le nom du participant
        while True:
            nom = input("Entrer le nom du participant à ajouter : ")
            if len(nom) != 0:
                nom = nom.capitalize()
                break
            print("Entrer une chaine non vide")
        # fin de la saisie du nom
        print("Dans quel groupe voulez-vous l'ajouter ? ")
        print(" 1 - Python")
        print(" 2 - Java")
        print(" 3 - web")

        # lecture sécurisée du choix
        while True:
            try:
                groupe = int(input("Votre  choix : "))
                if groupe in range(1, 4):
                    break
                print("Veuillez entrer un nombre entre 1 et 3")
            except ValueError:
                print("Veuillez entrer un nombre valide")
        # fin de la lecture

        if groupe ==1:
            python.add(nom)
            print(f"{nom} a été ajouté au groupe Python")
        elif groupe ==2:
            java.add(nom)
            print(f"{nom} a été ajouté au groupe Java")
        else:
            web.add(nom)
            print(f"{nom} a été ajouté au groupe Web")

        input("Retour au menu principal")
    elif choix == 3:
        # Supprimer un participant

        print("Supprimer un participant")
        # saisir le nom du participant
        while True:
            nom = input("Entrer le nom du participant à rechercher : ")
            if len(nom) != 0:
                nom = nom.capitalize()
                break
            print("Entrer une chaine non vide")
        # fin de la saisie du nom
        print("Dans quel groupe voulez-vous le supprimer ? ")
        print(" 1 - Python")
        print(" 2 - Java")
        print(" 3 - web")

        # lecture sécurisée du choix
        while True:
            try:
                groupe = int(input("Votre  choix : "))
                if groupe in range(1,4):
                    break
                print("Veuillez entrer un nombre entre 1 et 3")
            except ValueError:
                print("Veuillez entrer un nombre valide")
        # fin de la lecture

        if groupe ==1:
            if nom in python:
                python.remove(nom)
                print(f"{nom} a été supprimée du groupe Python")
            else:
                print(f"{nom} n'est pas dans le groupe Python")

        elif groupe ==2:
            if nom in java:
                java.remove(nom)
                print(f"{nom} a été supprimée du groupe Java")
            else:
                print(f"{nom} n'est pas dans le groupe Java")
        else:
            if nom in web:
                web.remove(nom)
                print(f"{nom} a été supprimée du groupe web")
            else:
                print(f"{nom} n'est pas dans le groupe web")

        input("Retour au menu principal")
    elif choix == 4:
        # Rechercher un participant

        print("Rechercher un participant")
        # saisir le nom du participant
        while True:
            nom = input("Entrer le nom du participant à rechercher : ")
            if len(nom)!=0:
                nom = nom.capitalize()
                break
            print("Entrer une chaine non vide")
        # fin de la saisie du nom
        # Rechercher s'il est présent dans l'ensemble python
        if nom in python:
            print(f"{nom} est dans le groupe python")

        # Rechercher s'il est présent dans l'ensemble java
        if nom in java:
            print(f"{nom} est dans le groupe java")


        # Rechercher s'il est présent dans l'ensemble web
        if nom in web:
            print(f"{nom} est dans le groupe web")

        # présent dans aucun groupe
        if nom not in python and nom not in java and nom not in web:
            print(f"{nom} n'est dans aucun groupe")
        input("Retour au menu principal")
    elif choix == 5:
        # Participants communs a l'ensemble des activités
        print("Participants communs")
        # mise en place d'un ensemble E4, qui contient l'intersection des ensembles
        # (python ET web) ET java
        E4 = (python.intersection(web)).intersection(java)
        print("La liste des participants")
        for participant in E4:
            print(f"- {participant}")
        input("Retour au menu principal")

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


