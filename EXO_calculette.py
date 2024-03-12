# Entrer les nombres en format Chiffre (Int ou Float)
a = float(input("Entrez un nombre A : "))
b = float(input("Entrez un nombre B : "))

operation = input("Choisissez le type d'operation (A S M D) : ")

operation = (operation.upper()) # majuscule obligatoire

if operation == "A":
  total = a + b # Addition
elif operation == "S":
  total = a - b # Soustraction
elif operation == "M":
  total = a * b # Multiplication
elif operation == "D":
  total = a / b # Division

print(total)