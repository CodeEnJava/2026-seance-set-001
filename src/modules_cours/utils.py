
import platform
import subprocess

# Module N°2
# Sa responsabilité : l'effacement de l'écran du terminal
# Ce module pourra être utilisé dans d'autre projet

def clear_screen():
    '''
    Cette fonction à pour but d'effacer l'écran du terminal
    :return: None
    '''
    if platform.system() == "Windows":
        subprocess.run("cls", shell=True)
    else:
        subprocess.run("clear", shell=True)