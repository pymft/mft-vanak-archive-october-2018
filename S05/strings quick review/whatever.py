text = """April is the cruelest month.
Breeding Lilacs out of the dead land"""

pattern = 'the'
loc = 0
occurrences = []
while True:
    loc = text.find('the', loc+1)
    if loc == -1:
        break
    occurrences.append(loc)

print(occurrences)