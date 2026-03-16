annuaire = {
    "jean" : "92228502",
    "paul" : "92027868",
    "marie" : "70117031"
}

nom = input("nom :")

num = annuaire.get(nom , "pas trouver")
print (num)