# PYTHON FONCTIONS : NOTIONS AVANCÉES
#
# CALLBACK
#

def ma_fonction():
    print("toto")
    return 1

a = 5

b = ma_fonction

print("a",a,"b",b())

# On stocke la fonction ma_fonction dans la variable b (sans les parenthèses)
# Ensuite, quand on fait b(), on exécute la fonction
# C’est le principe utilisé dans les callbacks : on passe une fonction sans l’exécuter,
# puis on l’appelle plus tard avec les parenthèses