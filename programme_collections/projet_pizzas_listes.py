
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


pizzas = ("4 fromages", "végétarienne", "hawai", "calzone")
vide =()
afficher(vide)