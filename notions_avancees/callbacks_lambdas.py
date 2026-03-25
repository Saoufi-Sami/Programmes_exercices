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



'''def mult_callback(a,b):
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
afficher_table(2,"*",power_callback)'''

# Au lieu de créer une fonction différente pour chaque opération,
# on fait une fonction générique (afficher_table)
# à laquelle on passe une fonction (callback) en paramètre.
# Cette fonction callback sera appelée à l’intérieur pour faire le calcul.
# Ça permet de réutiliser le même code avec des comportements différents.

# Exemple concret pour comprendre les callbacks et le fameux ( appeler plus tard ) :
#
# Imagine une porte :
# - "ouvrir_porte" = action d’ouvrir la porte
# - "quelqu’un sonne" = moment déclenché dans le code (comme un print)
#
# Exemple :
#
# def attendre_qu_on_sonne(action):
#     print("Quelqu’un sonne")   # événement (comme "début")
#     action()                   # on ouvre la porte à ce moment-là
#
# Ici, on passe la fonction SANS parenthèses :
# attendre_qu_on_sonne(ouvrir_porte)
#
# → ouvrir_porte n’est PAS exécutée tout de suite
# → elle sera exécutée PLUS TARD, au moment où "quelqu’un sonne"
#
# Par contre si on met des parenthèses :
# attendre_qu_on_sonne(ouvrir_porte())
#
# → ouvrir_porte() s’exécute DIRECTEMENT (avant même "quelqu’un sonne") ❌
#Avant le callback (action()), d’autres fonctions peuvent s’exécuter comme verifier_identite(), puis seulement après on appelle le callback
# Conclusion :
# - sans () → on passe une action (callback)
# - avec () → on exécute immédiatement

def afficher_table(n,operateur_str,operateur_cbk):
    for i in range(1,10):
        print(i,operateur_str,n,"=",operateur_cbk(i,n))


afficher_table(2,"x",lambda a, b : a * b)
print()
afficher_table(2,"+",lambda a, b : a + b)
print()
afficher_table(2,"*",lambda a, b : pow(a, b))

# Ici on utilise des lambda (fonctions rapides sans nom)
# au lieu de définir des fonctions à part.
# Ça permet d’écrire le callback directement, plus court et plus pratique.
# lambda = fonction rapide écrite directement comme callback