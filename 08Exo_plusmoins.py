nombre_mystere = 15
nombre_user = int(input("Entrez un nombre "))

if nombre_user == nombre_mystere:
  print("Ok, trouvé")
elif nombre_user > nombre_mystere:
  print("Plus bas")
elif nombre_user < nombre_mystere:
  print("Plus haut")
