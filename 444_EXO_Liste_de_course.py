liste_course = []
choix = 0

while True:
  print ("Choisissez parmi les 5 options suivantes : ")
  print("1/ Ajouter un élément à la liste")
  print("2/ Retirer un élement de la liste")
  print("3/ Afficher la liste")
  print("4/ Vider la liste")
  print("5/ Quitter")
  choix = int(input("choix : "))
  if choix == 1:
    element = input("Element à ajouter à la liste : ")
    liste_course.append(element)
  elif choix == 2:
    element = input("Element à supprimer à la liste : ")
    liste_course.remove(element) # a améliorer : afficher la liste et proposer les elements supprimable
  elif choix == 3:
    print(liste_course)
  elif choix == 4:
    liste_course = []
  elif choix == 5:
    break
  else :
    print("Veuillez entrez un choix")