# PYTHON FONCTIONS : NOTIONS AVANCÉES
#
# CALLBACK
#

'''def ma_fonction():
    print("toto")
    return 1

a = 5

b = ma_fonction

print("a",a,"b",b())'''

# On stocke la fonction ma_fonction dans la variable b (sans les parenthèses)
# Ensuite, quand on fait b(), on exécute la fonction
# C’est le principe utilisé dans les callbacks : on passe une fonction sans l’exécuter,
# puis on l’appelle plus tard avec les parenthèses



def mult_callback(a,b):
    return a*b

def add_callback(a,b):
    return a+b

def power_callback(a,b):
    return a,b

def afficher_table(n,operateur_str,operateur_cbk):
    for i in range(1,10):
        print(i,operateur_str,n,"=",operateur_cbk(i,n))


afficher_table(2,"x",mult_callback)
print()
afficher_table(2,"+",add_callback)
print()
afficher_table(2,"*",power_callback)

# Au lieu de créer une fonction différente pour chaque opération,
# on fait une fonction générique (afficher_table)
# à laquelle on passe une fonction (callback) en paramètre.
# Cette fonction callback sera appelée à l’intérieur pour faire le calcul.
# Ça permet de réutiliser le même code avec des comportements différents.