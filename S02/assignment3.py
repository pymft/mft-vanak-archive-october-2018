people = list("<<<<<<<><>>>><><>>>><><><>")
people_new = people.copy()


for j in range(20):
    for i in range(len(people)-1):
        if people[i] == '>' and people[i+1] == '<':
            people_new[i] = '<'
            people_new[i+1] = '>'

    people = people_new
    print(''.join(people))
