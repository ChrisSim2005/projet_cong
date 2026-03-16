📦 STRUCTURE ATTENDUE
text
bibliotheque/
│
├── main.py              # Point d'entrée
├── models/
│   ├── __init__.py
│   ├── livre.py         # Classe Livre
│   └── membre.py        # Classe Membre + dérivées
├── services/
│   ├── __init__.py
│   └── bibliotheque.py  # Logique métier
├── data/
│   └── bibliotheque.json # Fichier de données
└── tests/               # (Bonus)
    └── test_bibliotheque.py



🔧 PARTIE 1 : MODÈLES 
Classe Livre 
python
"""
Créez une classe Livre avec les attributs :
- id (auto-généré)
- titre (string)
- auteur (string)
- annee (int, 1900-2025)
- isbn (string, 13 chiffres)
- disponible (booléen)

Ajoutez :
- Constructeur avec validation
- Méthode __str__()
- Propriétés avec getters/setters
- Méthode to_dict() / from_dict()
"""
Classe Membre 
python
"""
Créez une classe abstraite Membre avec :
- id (auto-généré)
- nom (string)
- email (valide)
- date_adhesion (date)
- emprunts (liste)

Méthodes abstraites :
- peut_emprunter() -> bool

Classes dérivées :
- Etudiant (limite = 3 livres)
- Professeur (limite = 5 livres)
- Externe (limite = 2 livres, caution)
"""
Énumérations (1 point)
python
"""
Créez des énumérations pour :
- CatégorieLivre (ROMAN, SCIENCES, HISTOIRE, etc.)
- StatutMembre (ACTIF, SUSPENDU, RADIE)
"""


⚙️ PARTIE 2 : SERVICES 
Classe Bibliotheque 
python
"""
Créez la classe principale avec :

1. Gestion des livres :
   - ajouter_livre(livre)
   - supprimer_livre(id)
   - rechercher_par_titre(texte)
   - rechercher_par_auteur(nom)
   - rechercher_par_categorie(cat)
   - livres_disponibles()
   - livres_empruntes()

2. Gestion des membres :
   - inscrire_membre(membre)
   - radier_membre(id)
   - rechercher_membre(nom)

3. Gestion des emprunts :
   - emprunter_livre(id_membre, id_livre)
   - retourner_livre(id_livre)
   - prolonger_emprunt(id_livre, jours)
   - historique_membre(id_membre)

Règles métier :
- Un membre ne peut pas emprunter si suspendu
- Un livre non disponible ne peut être emprunté
- Durée max : 15 jours (étudiant), 30 jours (prof)
- Retard = suspension automatique
"""
Validation et Utilitaires 
python
"""
Créez des fonctions de validation :
- valider_email(email) -> bool
- valider_isbn(isbn) -> bool
- valider_annee(annee) -> bool
- formater_nom(nom) -> string
- calculer_retard(date_retour) -> int
"""


💾 PARTIE 3 : PERSISTANCE 
python
"""
Implémentez la sauvegarde/chargement JSON :

1. Sauvegarder l'état complet :
   - Livres
   - Membres
   - Emprunts en cours

2. Charger au démarrage
3. Sauvegarde automatique après chaque modification

Format JSON :
{
    "livres": [...],
    "membres": [...],
    "emprunts": [...],
    "statistiques": {...}
}
"""


🖥️ PARTIE 4 : INTERFACE 
python
"""
Créez une interface console avec :

MENU PRINCIPAL
==============
1. Gestion des livres
2. Gestion des membres
3. Gestion des emprunts
4. Statistiques
5. Sauvegarder
6. Quitter

SOUS-MENUS avec options CRUD complètes

Exigences :
- Navigation intuitive
- Messages clairs
- Confirmation avant actions importantes
- Retour au menu principal après chaque action
"""


⚠️ PARTIE 5 : GESTION D'ERREURS 
python
"""
Gérez tous les cas d'erreur :

- Fichier de données inexistant
- ISBN invalide
- Email mal formaté
- Membre inexistant
- Livre déjà emprunté
- Limite d'emprunts atteinte
- Saisies utilisateur incorrectes
- Dates invalides

Utilisez des exceptions personnalisées :
- LivreNonTrouveError
- MembreNonTrouveError
- EmpruntImpossibleError
- FichierCorrompuError
"""


📊 PARTIE 6 : STATISTIQUES 
python
"""
Générez des statistiques :
- Nombre total de livres
- Nombre de livres par catégorie
- Membres les plus actifs
- Livres les plus empruntés
- Taux d'occupation
- Retards en cours
"""


🎯 EXEMPLE D'EXÉCUTION
text
===========================================
    BIBLIOTHÈQUE MUNICIPALE - v2.0
===========================================

MENU PRINCIPAL :
1. Gestion des livres
2. Gestion des membres
3. Gestion des emprunts
4. Statistiques
5. Sauvegarder
6. Quitter

Votre choix : 1

--- GESTION DES LIVRES ---
1. Ajouter un livre
2. Modifier un livre
3. Supprimer un livre
4. Rechercher un livre
5. Afficher tous les livres
6. Retour

Choix : 4

Recherche par : 1. Titre  2. Auteur  3. Catégorie : 1
Titre à rechercher : "python"

Résultats (3 livres) :
----------------------------------------
1. "Python pour les nuls" - J. Dupont (2023) [Disponible]
2. "Apprendre Python" - M. Martin (2022) [Emprunté - retour: 15/03]
3. "Python avancé" - P. Durand (2024) [Disponible]
----------------------------------------

Appuyez sur Entrée pour continuer...