usernames = []

if usernames:
    for username in usernames:
        if username == "admin":
            print (f"\nHello {username}, would you like to see a status report?")
        else:
            print (f"\nHello {username}, thank you for loggin on again!")
else:
    print ("We need to find some users!")