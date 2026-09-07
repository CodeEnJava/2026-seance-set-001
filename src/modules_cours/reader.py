
# Module 4
# Sa responsabilité : la saisie d'informations par l'utilisateur

def read_integer_min_max(str_message,mini,maxi):
    while True:
        try:
            value = int(input(str_message))
            if value in range(mini, maxi):
                return value
            print(f"Veuillez entrer une valeur comprise entre {mini} et {maxi-1}")
        except ValueError:
            print("Veuillez entrer un nombre valide")




