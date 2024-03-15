liste = ["1", "4", "25", "Paul", "3", "Pierre"]
for element in liste:
	if element.isdigit():
		continue 
	print(element)
	

# continue renvoie directement vers la boucle for sans finir l'instruction
# remplacer continue par break
