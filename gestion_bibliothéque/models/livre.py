class Livre:
 def __init__(self, id , titre, auteur, annee, isbn, disponible):
  
  if len(titre) ==0 or len(auteur) == 0:
    raise ValueError("le titre et l'auteur ne peuvent pas etre vides")
  
  if annee < 1900 or annee >2025:
    raise ValueError("l'année doit être comprise entre 1900 et 2025")
  
  if len(isbn) != 13 or not isbn.isdigit():
    raise ValueError("l'ISBN doit être un nombre de 13 chiffres")
  
  self.id=id
  self.titre=titre
  self.auteur=auteur
  self.annee=annee
  self.isbn=isbn
  self.disponible=disponible


  def __str__(self):
    print("id" ,self.id , "titre" , self.titre , "auteur" , self.auteur , "annee" , self.annee , "isbn" , self.isbn , "disponible" , self.disponible)

