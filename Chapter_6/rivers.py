rivers = {
    'nile': 'egypt',
    'thames': 'england',
    'ganges': 'india',
    'yangtze': 'china',
    'zanbezi': 'africa',
}

for river, country in rivers.items():
    print (f"\nRiver Name: {river.title()}")
    print (f"Country: {country.title()}")