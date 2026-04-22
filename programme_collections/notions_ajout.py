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

# Tris : Sort / Sorted

#          0         1         2            3         4
noms = ["Jean" , "Sophie" , "Martin", "Christophe", "Zoe"]

noms.sort(reverse=True) #in place ici on tri sur la liste principal sort tri par ordre alphabetique et du plus petit au plus grand
noms_tries = sorted(noms, reverse=True) # on cree une nouvelle liste

print(noms)
print(noms_tries)

# operations sur les éléments : min,max, in, sum
# Swapper deux éléments (échanger)
noms[0], noms[4] = noms[4],noms[0]
# join : rejoindre -> coller et split -> separer
noms_join = ', '.join(noms)
print(noms_join)
a = "Paul-Marc-Emilie"
a_split = a.split("-")
print(a_split)
# index, find et count
# Les compréhension de listes
# pour avoir par ex la longueur des caracteres de chaque mot on va faire simplement : longeur_noms = [len(nom) for nom in noms], en gros c'est une sintaxe bcp plus consise
# print(longeur_noms)
# Any et All n'importe quelle et tous
nom_avec_un_z_existe = all([True if "z" in nom.lower() else False for nom in noms])
if nom_avec_un_z_existe:
    print("Trouvé")
else:
    print("non trouvé")
# Any des qu'il trouve un true quelqupart il return true et isdigit il retourne true si il ya un chiffre
