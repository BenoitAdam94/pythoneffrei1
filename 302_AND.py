utilisateur = input("Nom d'utilisateur : ")
mot_de_passe = input("Mot de Passe : ")

# avec 2 if
if utilisateur == "admin":
	if mot_de_passe == "mdp":
		print("Accès autorisé")

# simplification avec AND
if utilisateur == "admin" and mot_de_passe == "mdp":
	print("Accès autorisé")
