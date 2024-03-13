mon_tuple = (1, 2, 3)
mon_tuple = (250, "Python", True)

# Il est possible de convertir un tuple en liste
# et vice-versa grâce aux fonctions list et tuple:

mon_tuple = (1, 2, 3)

liste = list(mon_tuple)

liste.append(4)

mon_tuple = tuple(liste)

print(mon_tuple)

