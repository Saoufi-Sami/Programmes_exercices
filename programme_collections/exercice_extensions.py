# LES COLLECTIONS : LISTES / TUPLES
# Exercice "Extraire les extensions"



fichiers = ("notepad.exe", "mon.fichier.perso.doc", "notes.TXT", "vacances.jpeg", "planning", "data.dat")

definition_extensions = (("doc", "Document Word"),
                        ("exe", "Executable"),
                        ("txt", "Document Texte"),
                        ("jpeg", "Image JPEG"))

"""definition_extensions_dict = {"doc": "Document Word",
                        "exe": "Executable",
                        "txt": "Document Texte",
                        "jpeg": "Image JPEG"}"""



# Version 1 : boucle classique
# Ici, chaque "element" est un tuple comme ("doc", "Document Word")
# On doit accéder aux valeurs avec des index :
# element[0] = extension
# element[1] = description

#for element in definition_extensions:
 #   if extension == element[0]:
 #       print(fichier + " (" + element[1] + ")")



for fichier in fichiers:
    trouve = False
    if ("." in fichier):
        extension = fichier.split(".")[-1].upper()
        for ext, description in definition_extensions:
            if extension == ext.upper():
                trouve=True
                print (fichier + " (" + description + ")")
        if not trouve:
         print(fichier + " (Extension non connue)")

    else :
        print (fichier + " (Aucune extension)")
# Version 2 : unpacking (déballage)
# Python "ouvre" directement le tuple pour nous
# ext = element[0]
# description = element[1]
# => code plus lisible et plus propre
















'''
notepad.exe (Executable)
mon.fichier.perso.doc (Document Word)
notes.TXT (Document Texte)
vacances.jpeg (Image JPEG)
planning (Aucune extension)
data.dat (Extension non connue)
'''

# lower/upper
# in / index / for
# split
# -1

# extraire extension



# faire la correspondance définition

