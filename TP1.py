### Logique métier ###
#Compter le nombre de lignes
def lire_log() :
    try :
        with open ("network_log.txt", "r") as f:
                return f.readlines()
    except FileNotFoundError as err :
        print(f"Erreur d'ouverture de fichier log # {err}")
    return []

def nombre_lignes() :
    return len(lire_log())
        
#Compter le nombre de connexions par protocole
def nombre_connexions() :
    protocoles = {}
    for ligne in lire_log() :
        protocole = ligne.split( )[-1]
        if protocole in protocoles.keys() :
            protocoles[protocole] += 1
        else :
            protocoles[protocole] = 1
    return protocoles.items()

#Affichage des données analysées
print(f"{nombre_lignes()} connexions au total, dont :")
for item, value in nombre_connexions() :
    print(f"{item} : {value}")


"""
#Identifier et stocker toutes les adresses IP uniques (set)
source_IPs = set()
destination_IPs = set()
for ligne in lire_log() :
    mots = ligne.split( )
    source_IPport = mots[2]
    destination_IPport = mots[4]
    source = source_IPport.split(":")
    destination = destination_IPport.split(":")
    source_IP = source[0]
    destination_IP = destination[0]
    source_IPs.add(source_IP)
    destination_IPs.add(destination_IP)
all_IPs = source_IPs|destination_IPs
print(source_IPs)
print(destination_IPs)
print(all_IPs)
"""


while (True) :
    # Imput utilisateur demandant une IP spécifique
    numero_ligne = -1
    input_IP = input("Veuiller entrer l'IP à rechercher : ")
    
    #recherche de toutes les connexions impliquant l'IP inputé
    for ligne in lire_log() :
        numero_ligne += 1
        mots = ligne.split( )
        source_IPport = mots[2]
        destination_IPport = mots[4]
        source = source_IPport.split(":")
        destination = destination_IPport.split(":")
        source_IP = source[0]
        destination_IP = destination[0]
        if str(input_IP) == str(source_IP) or str(input_IP) == str(destination_IP) :
            print(lire_log()[numero_ligne])

### Gestion des erreurs ###
#Fichier inexistant
#Fichier vide
#IP invalide (ajouter tentative de conversion automatique du format IP ?)
#IP introuvable

