interval = range(10) # ou range(0, 10)
"""
print(interval)
print(type(interval))
print(interval.start)
print(interval.step)
print(interval.stop)
"""

# Si vous souhaitez récupérer cet objet 
# range sous la forme d'une liste, il suffit de le convertir avec la fonction list :

interval = list(interval)
print(interval)
print(type(interval))