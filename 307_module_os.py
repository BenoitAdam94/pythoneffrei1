import os

chemin = ""

dossier = os.path.join(chemin, "dossier")
# slash sur windows et mac ne sont pas dans le même sens (join)

print(dossier)

# Si le dossier n'existe pas :
if not os.path.exists(dossier):
  os.makedirs(dossier) # crée le dossier

# Si le dossier existe :
if os.path.exists(dossier):
  os.removedirs(dossier) # suprrime le dossier










# if not os.path.exists(dossier);
# os.makedirs(dossier) # crée le dossier

# if os.path.exists(dossier);
# os.removedirs(dossier)
