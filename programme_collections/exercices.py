# LISTES - EXERCICE : DEMANDER NOMS DE PERSONNES

# nom et age avec input
''' for i in range (3):
       nom = input("Nom de la personne : ")
       print("Le nom est :", nom) '''

# demander des noms de personnes
# boucle infinie, sort quand le nom est vide == "" => break
# seulement à la fin afficher tout les noms

noms = []

while True:
    nouveau_nom = input("Nom de la personne : ")
    if nouveau_nom == "":
        break
    noms.append(nouveau_nom)

print()
print("Noms des personnes :")
noms.sort() # ordre alphabetique A-Z a-z
for nom in noms:
    print("    " + nom)











