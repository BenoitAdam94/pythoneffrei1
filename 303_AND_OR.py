x = 1
y = 0
z = 0

if x == 1 and y == 1:
	print("X et y sont a 1")

if x == 1 or y == 1:
	print("X et/ou y est a 1")

# and est prioritaire, mais le mieux est d’utiliser des parenthèses

if x == 1 and y == 1 or z == 0:
	print("Hello World")