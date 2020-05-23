current_users = ['Inspiration','sSupremee','Denzaaaaal','radbrad','tcole']
new_users = ['denzaaaaal', 'neb', 'inspiration','stiscott', 'cdiamond']

# Ensureing all characters is lower case
taken_usernames = []
for current_user in current_users:
    taken_usernames.append(current_user.lower())

# Checking 
for new_user in new_users:
    if new_user in taken_usernames:
        print (f"Username {new_user} taken! Please select another username")
    else:
        print (f"Username {new_user} available. Would you like to select that username?")