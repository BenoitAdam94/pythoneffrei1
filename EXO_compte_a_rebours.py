import time #importe le module time
from time import sleep #importe uniquement le nécessaire du module time

x = 3

for i in range(0, 3):
  print(x)
  time.sleep(1)
  x = x-1
  
print("Go !!")