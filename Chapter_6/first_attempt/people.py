# Creating dictionary of each
person_0 = {
    'first_name': 'paul',
    'last_name': 'carter',
    'age': '28',
    'city': 'Orpington'
}

person_1 = {
    'first_name': 'cheryl',
    'last_name': 'mccook',
    'age': '59',
    'city': 'Bellingham'
}

person_2 = {
    'first_name': 'laverne',
    'last_name': 'douglas',
    'age': '33',
    'location': 'bellingham'
}

# Creating a list with all the people
people = [person_0, person_1, person_2]

# printing out the values
for person in people:
    for detail in person.values():
        print (f"First name: {detail['first_name']}")