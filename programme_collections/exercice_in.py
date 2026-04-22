# LES COLLECTIONS : LISTES / TUPLES
# Exercice "in insensible a la casse"


def element_dans_liste(e, l):
    for i in l:
        if e.lower() == i.lower():
            return True

    return False

# On parcourt chaque élément de la liste `l`.
# Pour chaque élément, on le compare avec `e` en les mettant tous les deux en minuscules (grâce à lower())
# afin d’ignorer les différences entre majuscules et minuscules.
# Si on trouve une correspondance, on arrête la fonction et on retourne True.
# Si la boucle se termine sans trouver de correspondance, on retourne False (l’élément n’est pas dans la liste).

#         0         1        2            3         4       5
noms = ["Jean", "Sophie", "Martin", "Christophe", "Zoe", "Martin"]

if element_dans_liste("JeAn", noms):
    print("Jean is here")
else:
    print("Jean is not here")