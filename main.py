import time

print("== Calculateur de dépenses ==")
total = 0 
while True:
    try:
        budget_input = input("quel est votre budget mensuel : ")
        
        # Vérifier les zéros en début (sauf pour 0.x)
        if budget_input.startswith('0') and len(budget_input) > 1 and not budget_input.startswith('0.'):
            print("Ne commencez pas par zéro (sauf pour les décimales comme 0.5)")
            continue
            
        budget = float(budget_input)
        if budget <= 0:
            print("le budget doit etre positif ")
            continue
        break
    except ValueError:
        print("Entrez un nombre valide")
        break


dep = int(input("Quelle est votre nombre de dépenses : "))

categorie = {1: "Nourriture", 2: "logement", 3: "transport", 4: "loisirs"}
montants = {1: 0, 2: 0, 3: 0, 4: 0}

for i in range(dep):
    print("[depense", i+1, "]")
    montant = float(input("le montant: "))
    cat = int(input("la catégorie (Nourriture = 1, logement = 2, transport = 3, loisirs = 4) : "))
    if cat in montants:
        montants[cat] += montant
        total += montant
        reste = budget - total
        print("Total :" ,total)
        print("reste :" , reste)
        print("catégorie :" , categorie[cat])

print("Calcul en cours...")
time.sleep(3)
print("=Recapitulatif=")
print("votre total de dépenses est de :" , total)
print("il vous reste :" , reste)
for cat in categorie:
    print(categorie[cat] , ":" , montants[cat])
    


