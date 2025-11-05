#Exo1-1 (module pathlib)
from pathlib import Path

def lire_log(name) :

    try :

        with open("network_log.txt","r") as f:

            return f.readlines()

    except FileNotFoundError as err :

        print(f"Erreur d'ouverture de fichier log # {err}")    

    return []
 
 
def nb_lignes_log(name):

    return len(lire_log(name))
 
def connexion_par_protocole() :

    pass

FILE_LOG = "network_log.txt"

#print(os.path.abspath(FILE_LOG))  

print(f"Nombre de lignes Log : {nb_lignes_log((Path(FILE_LOG))) }")
 