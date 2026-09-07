
# les données pour les menus utilisées dans l'affichage

# Le menu principal
main_title = "GESTION DES PARTICIPANTS"
main_items = [
                "Afficher les participants",
                "Ajouter un participant",
                "Supprimer un participant",
                "Rechercher un participant",
                "Participants communs",
                "Statistiques",
                "Quitter"
            ]
# mettre en place une liste composée de deux éléments
# un titre
# la liste des items

main_menu =[main_title.upper(),main_items]

# le sous menu :Afficher les participants

sub_title = "Requête d'affichage des participants"
sub_items = [
                "Afficher les participants du groupe Python",
                "Afficher les participants du groupe Java",
                "Afficher les participants du groupe Web",
                "Afficher les participants de tous les groupes",
                "Afficher les participants en fonction d'une requête",
                "Retour au menu principal"
            ]

sub_menu= [sub_title.upper(),sub_items]

