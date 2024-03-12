import random

a = random.randint(0, 1) # entier 0 et 1
print(a)

b = random.uniform(0, 1) # float entre 0 et 1
print(b)

c = random.randrange(5) # exclusif (5 ne sortira jamais)
print(c)

d = random.randrange(0, 101, 10) # 0 a 100 de 10 en 10
print(d)
