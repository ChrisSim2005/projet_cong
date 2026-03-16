📝 Plan de développement


Jour 1 : Les bases

Créer une variable total = 0
Demander "Combien as-tu dépensé ?" → montant = input()
Convertir en nombre → float(montant)
Ajouter au total → total = total + montant
Afficher le total

Jour 2 : Plusieurs dépenses

Ajouter une boucle while True
Demander "Veux-tu ajouter une dépense ? (o/n)"
Sortir de la boucle si l'utilisateur dit "n"
Calculer la moyenne des dépenses

Jour 3 : Les catégories

Créer un dictionnaire : categories = {"nourriture": 0, "transport": 0, ...}
Pour chaque dépense, demander la catégorie
Ajouter le montant à la bonne catégorie
Afficher le total par catégorie

Jour 4 : Budget et alertes

Demander un budget mensuel au démarrage
Calculer le budget restant
Alerter si dépense > budget restant
Bloquer si budget dépassé

Jour 5 : Sauvegarde

Écrire les données dans un fichier à la fin
Lire les données au démarrage
Ajouter les dates

🎮 Exemple d'utilisation
=== CALCULATEUR DE DÉPENSES ===

Votre budget mensuel fixé : 500€
combien de dépense avez vous fais : 2


[Dépense 1]
Montant : 25.50
Catégorie (1-nourriture, 2-transport, 3-loisirs) : 1
✅ Ajouté : 25.50€ en nourriture

[Dépense 2]
Montant : 12.80
Catégorie : 2
✅ Ajouté : 12.80€ en transport

Récapitulatif :
- Nourriture : 25.50€
- Transport : 12.80€
- Loisirs : 0€
TOTAL : 38.30€
Budget restant : 461.70€

Veux-tu ajouter une autre dépense ? (o/n) : n

Au revoir !