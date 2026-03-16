import random
import string
import time

def mot_de_passe(longueur):
    lettre = string.ascii_lowercase + string.ascii_uppercase + string.digits + string.punctuation
    mot = ""
    for i in range(longueur):
        carat_aleatoire = random.choice(lettre)
        mot += carat_aleatoire
    print("Génération en cours...")
    time.sleep(2)
    return mot
    
print("Quelle est la longueur de votre mot de passe ?")
longueur = int(input("longueur : "))

print("votre mot de passe est : " + mot_de_passe(longueur))
