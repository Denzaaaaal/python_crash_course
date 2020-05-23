pet_0 = {
    'name': 'lele',
    'type': 'leopard',
    'mother': 'laverne',
}
pet_1 = {
    'name': 'tigger',
    'type': 'tiger',
    'mother': 'laverne',
}
pet_2 = {
    'name': 'rexy',
    'type': 'dinosaur',
    'mother': 'laverne',
}
pet_3 = {
    'name': 'owly',
    'type': 'owl',
    'mother': 'laverne',
}
pet_4 = {
    'name': 'pugster',
    'type': 'dog',
    'mother': 'laverne',
}

pets = [pet_0, pet_1, pet_2, pet_3, pet_4]

for pet in pets:
    print (f"\nHi, My name is {pet['name'].title()}!")
    print (f"The type of animal I am is a {pet['type'].title()} "
            f"and my mother is called {pet['mother'].title()}.")