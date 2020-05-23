favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python',
}

people = ['frank', 'jen', 'denzel', 'jordon', 'phil']


for person in people:
    print (f"\nHi {person.title()}")
    if person in favorite_languages.keys():
        print ("Thanks for taking our poll")