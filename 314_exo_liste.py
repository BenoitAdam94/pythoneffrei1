liste = ["Maxime", "Martine", "Christopher", "Carlos", "Michael", "Eric"]

# L'objectif de cet exercice est de récupérer les informations
# suivantes grâce aux slices :

# Les trois premiers employés ("Maxime", "Martine" et "Christopher")
trois_premiers = liste[0:3]
# Les trois derniers employés ("Carlos", "Michael" et "Éric")
trois_derniers = liste[3:]
# Tous les employés sauf le premier et le dernier dans une liste milieu
milieu = liste[1:5]
# Le premier et le dernier employé dans une liste premier_dernier
premier_dernier = liste[::5]

print(trois_premiers)
print(trois_derniers)
print(milieu)
print(premier_dernier)