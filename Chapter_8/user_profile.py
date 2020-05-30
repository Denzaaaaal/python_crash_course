def build_profile(first, last, **user_info):
    """Building a dictionary containingg everything we know about a user"""
    user_info['first_name'] = first
    user_info['last_name'] = last
    return user_info

user_profile = build_profile('denzel', 'douglas',
                            location='london',
                            field='IT',
                            age=26)

print (user_profile)