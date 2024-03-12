carte = 20
plein = 10
reduit = 8

places = 0

while (carte + (places * reduit)) > (places * plein):
  places += 1
  print(places)


print(f"Il faut acheter au moins {places} places")