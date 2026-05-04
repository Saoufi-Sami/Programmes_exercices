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


for fichier in fichiers:
    trouve = False
    if ("." in fichier):
        extension = fichier.split(".")[-1].upper()
        for element in definition_extensions:
            if extension == element[0].upper():
                trouve=True
                print (fichier + " (" + element[1] + ")")
        if not trouve:
         print(fichier + " (Extension non connue)")

    else :
        print (fichier + " (Aucune extension)")



















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

