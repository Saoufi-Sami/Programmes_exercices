# PYTHON FONCTIONS : NOTIONS AVANCÉES
#
# DIFFERENCE ENTRE BREAK ET RETURN
#

def a():
    print("Debut de la fonction")
    for i in range (1,10):
        if i > 5 :
            break
        print(i)
    print("fin de la fonction")

a()

# "break" est utilisé uniquement dans une boucle (for ou while).
# Il sert à sortir immédiatement de la boucle,
# mais la fonction continue ensuite son exécution.


    # Si on mettait "return" à la place de "break",
    # la fonction s'arrêterait complètement ici.
    # Python sortirait immédiatement de la fonction
    # et la ligne "print('fin de la fonction')" ne serait jamais exécutée.

    # Contrairement à "break", "return" permet aussi
    # de renvoyer un résultat depuis la fonction
    # que l'on peut récupérer ailleurs dans le programme.