tva_reduite = 5 # TVA en pourcent
tva_pleine = 20
prix_ht = 0
prix_ttc = 0

def ajout_tva(prix_ht):
  if (type_tva == 1):
    prix_ttc = prix_ht * ((100 + tva_reduite)/100)
  elif (type_tva == 2):
    prix_ttc = prix_ht * ((100 + tva_pleine)/100)
  return prix_ttc

prix_ht = float(input("Entrez le Prix Hors-taxe : "))
type_tva = int(input("Entrez 1 pour la TVA réduite, 2 pour la TVA pleine "))

print ("Le prix TTC est " + str(ajout_tva(prix_ht)))
