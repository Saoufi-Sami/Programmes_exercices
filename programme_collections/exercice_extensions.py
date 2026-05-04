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



'''for fichier in fichiers:
    trouve_extension = False
    if ("." in fichier):
        extension = fichier.split(".")[-1].upper()
        for ext, description in definition_extensions:
            if extension == ext.upper():
                trouve_extension=True
                print (fichier + " (" + description + ")")
        if not trouve_extension:
         print(fichier + " (Extension non connue)")

    else :
        print (fichier + " (Aucune extension)")'''
# Version 2 : unpacking (déballage)
# Python "ouvre" directement le tuple pour nous
# ext = element[0]
# description = element[1]
# => code plus lisible et plus propre


def extraire_extension(nom_fichier):
        if ("." in nom_fichier):
            extension = nom_fichier.split(".")[-1].upper()
            return extension
        return None

def get_definition_extension(extension,definitions):
    for ext, description in definitions:
        if extension == ext.upper():
           return description
    return None


for fichier in fichiers:
    ext = extraire_extension(fichier)
    if ext:
        definition = get_definition_extension(ext, definition_extensions)
        if not definition:
            definition = "Extension non connue"
    else:
        definition = "Aucune extension"
    print(fichier + " (" + definition + ")")




