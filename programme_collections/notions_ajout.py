# LES COLLECTIONS : LISTES/TUPLES
# Append / Extend / += / Insert

noms = ["Jean" , "Sophie" , "Martin"]

noms_supplementaires = ["Christophe", "Zoe"]

#noms.append(noms_supplementaires)
# for e in noms_supplementaires:
#          noms.append(e)
# noms.extend(noms_supplementaires

# noms.append("Toto")
# noms.insert(1, "Toto")

noms = noms + noms_supplementaires
print(noms)



# Slices
noms = ["Jean" , "Sophie" , "Martin", "Christophe", "Zoe"]
slices_noms = noms[:]

noms[0] = "Toto"
print(noms)
print(slices_noms)
# noms[:] crée une COPIE de la liste (une nouvelle liste différente)
# donc quand on modifie "noms", ça ne change pas "slices_noms"

# voilà pourquoi les print ne sont pas les mêmes :
# - print(noms) affiche la liste modifiée
# - print(slices_noms) affiche l’ancienne version (copie non modifiée)

# alors que "slices_noms = noms" ferait pointer vers la même liste
# donc les deux print seraient identiques