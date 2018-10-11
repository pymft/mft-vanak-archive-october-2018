people = ">>><<<<<<<<<<>>>>><<<<<<<<<<<>><<<<<<"

for i in range(30000):
    people_new = people.replace('><', '<>')
    if people == people_new:
        break
    people = people_new
    print(people.replace('<>', '\/').replace('<', ' ').replace('>', ' '))