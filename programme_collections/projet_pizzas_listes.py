

def ajouter_pizzas_utilisateur(collection):
    p = input("Quelle pizza vous voulez ajouter ? ")
    if pizza_existe(p,collection) :
        print("ERREUR la Pizza existe deja")
    else:
        collection.append(p)

def pizza_existe(e,collection):
    if e in collection:
        return True
    else:
        return False


def afficher(collection):
    if not collection :
        print("AUCUNE PIZZA")
        return
    print(f"---- LISTE DES PIZZAS ({len(collection)}) ----")
    for i in collection:
        print(i)
    print()
    print("Premiere pizza : " + collection[0])
    print("Derniere pizza : " +collection[-1])


pizzas = ["4 fromages", "végétarienne", "hawai", "calzone"]
vide =()
ajouter_pizzas_utilisateur(pizzas)
afficher(pizzas)

'''if p == "":
    ajouter_pizzas_utilisateur(collection)
else:'''