person_0 = {
    'first_name': 'denzel',
    'last_name': 'douglas',
    'age': 25,
    'city': 'london',
}
person_1 = {
    'first_name': 'laverne',
    'last_name': 'douglas',
    'age': 33,
    'city': 'london',
}
person_2 = {
    'first_name': 'cheryl',
    'last_name': 'mccook',
    'age': 58,
    'city': 'london'
}

people = [person_0, person_1, person_2]

for person in people:
    print (f"\nMy first name is {person['first_name'].title()}")
    print (f"My last name is {person['last_name'].title()}")
    print (f"My age is {person['age']}")
    print (f"The city I live in is {person['city'].title()}")