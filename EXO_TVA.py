tva1 = 20 # TVA en pourcent
prix_ht = 0
prix_ttc = 0

def ajout_tva(prix_ht):
  prix_ttc = prix_ht * ((100 + tva1)/100)
  return prix_ttc

input_user = float(input("Entrez le Prix Hors-taxe : "))

print ("Le prix TTC est " + str(ajout_tva(input_user)))
