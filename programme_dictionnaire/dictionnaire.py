personne = {'nom':'Mélanie', 'age':25, 'taille':1.60}


personne['nom'] = 'calire'


achat = ('fromage','beurre')
(personne['achat']) = achat


poste =('Developpeur')
(personne['poste']) = poste
print(personne)

for i in personne:
    print(f"clef: {i} - valeur: {personne[i]}")
