rivers = {
    'nile': 'egypt',
    'thames': 'england',
    'black river': 'jamaica',
}


for river, country in rivers.items():
    print (f"The {river.title()} runs through {country.title()}")


print ("\nNow for the countries:")
for country in rivers.values():
    print (country)

print ("\nNow for the rivers")
for river in rivers.keys():
    print (rivers)