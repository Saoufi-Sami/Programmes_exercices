

def ajouter_pizzas_utilisateur(collection):
    reponse = input("Quelle pizza vous voulez ajouter ?")
    if reponse == "":
        ajouter_pizzas_utilisateur(collection)
    else:
     collection.append(reponse)


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