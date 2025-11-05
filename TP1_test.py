### Logique métier ###
#Compter le nombre de lignes
with open ("network_log.txt", "r") as f:
        lignes = f.readlines ()
        nombre_lignes = len(lignes)
        print(nombre_lignes)
        
#Compter le nombre de connexions par protocole
protocoles = {}
for ligne in lignes :
    mots = ligne.split( )
    protocole = mots[-1] #foreach sous-liste récupérer le dernier élément (protocol)
    if protocole in protocoles.keys() :
        protocoles[protocole] += 1
    else :
        protocoles[protocole] = 1
print(protocoles)

#Identifier et stocker toutes les adresses IP uniques (set)
source_IPs = set()
destination_IPs = set()
for ligne in lignes :
    mots = ligne.split( )
    source_IP = mots[2]
    destination_IP = mots[4]
    source_IPs.add(source_IP)
    destination_IPs.add(destination_IP)
print(source_IPs)
print(destination_IPs)


# Imput utilisateur demandant une IP spécifique

#recherche de toutes les connexions impliquant l'IP inputé


### Gestion des erreurs ###
#Fichier inexistant
#Fichier vide
#IP invalide (ajouter tentative de conversion automatique du format IP ?)
#IP introuvable

