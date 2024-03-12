import random # importer le module random

nombre_mystere = random.randint(1, 50)
nombre_user = 0

while nombre_mystere != nombre_user:
  nombre_user = int(input("Entrez un nombre "))
  if nombre_user == nombre_mystere:
    print("Trouvé !")
  elif nombre_user > nombre_mystere:
    print("Plus bas")
  elif nombre_user < nombre_mystere:
    print("Plus haut")
