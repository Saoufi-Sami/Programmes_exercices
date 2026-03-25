# PYTHON FONCTIONS : NOTIONS AVANCÉES
#
# Nombre de variable de paramètres

# Premiere methode :
'''def a (age, taille, poids):
    print("toto", age, taille, poids)

a(20,1,65)'''

# Deuxieme methode
'''def somme(*nombres):
    resultat = 0
    for n in nombres:
        resultat += n
    return resultat

print(somme(5,35,6,4,7,5,4))'''

# *nombres permet de passer un nombre variable d’arguments à la fonction
# Tous les arguments sont regroupés automatiquement dans un tuple appelé "nombres"
#
# Exemple :
# somme(5, 35, 6, 4) → nombres = (5, 35, 6, 4)
#
# Ensuite, la boucle "for n in nombres" parcourt chaque élément du tuple
# À chaque tour, "n" prend une valeur du tuple (5 puis 35 puis 6 etc.)
#
# On additionne chaque valeur dans la variable "resultat"
# puis on retourne le total à la fin avec "return resultat"


# Troisieme methode
def somme(titre,**nombres):
    resultat = 0
    for n in nombres.values():
        resultat += n
    return resultat

print(somme("somme des notes", maths=5,geo=12,anglais=6))

# **nombres permet de passer des arguments nommés (clé=valeur)
# Ils sont regroupés dans un dictionnaire "nombres"
#
# Exemple :
# somme("titre", maths=5, geo=12) → nombres = {"maths": 5, "geo": 12}
#
# .values() permet de récupérer uniquement les valeurs du dictionnaire
# si on avais fais .keys on recup les clé par ex = maths
# On parcourt ces valeurs avec une boucle pour faire la somme



















