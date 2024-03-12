#importer le module
import time
# temps écoulé depuis le 1er janvier 1970
print(time.time())
# temps détaillé
print(time.localtime(0))
#Afficher le jour de la semaine
print(time.strftime("%d/%m/%Y"))