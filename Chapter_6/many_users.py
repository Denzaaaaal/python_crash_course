users = {
    'aeinstien' : {
        'first': 'albert',
        'last': 'einstien',
        'location': 'prinction',
    },

    'mcurie': {
        'first': 'marie',
        'last': 'curie',
        'location': 'paris',
    }
}

for username, user_info in users.items():
    print (f"Username: {username}")
    full_name = f"{user_info['first']} {user_info['last']}"
    location = user_info['location']

    print (f"\tFull name: {full_name}")
    print (f"\tLocation: {location}")