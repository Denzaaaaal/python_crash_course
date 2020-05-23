cities = {
    'london': {
        'country': 'england',
        'population': 8.98,
        'fact': 'london is the smallest city in england'
    },
    'tokyo': {
        'country': 'japan',
        'population': 9.27,
        'fact': 'tokyo for fromally known as "edo" in the 20th century',
    },
    'malmo': {
        'country': 'sweden',
        'population': 0.3,
        'fact': 'malmo was originally Danish'
    },
}

for city, detail in cities.items():
    print (f"\nThis is the city of {city.title()}.")
    print (f"\tThis is located in the county of {detail['country'].title()}.")
    print (f"\tThis city has a population size of {detail['population']} Million.")
    print (f"\tAn interesting fact about the city is {detail['fact']}.")