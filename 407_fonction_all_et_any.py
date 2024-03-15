any([False, False, True, False])

all([False, False, True, False])

# exemple 1
# all([f.endswith(".jpg") for f in files])

# exemple 2
notes = [12, 14, 20, 10, 8]
notes2 = any([x > 18 for x in notes])

print(notes2)
