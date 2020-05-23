flag = True
while flag == True:

    age = input("\nPlease enter the person age: ")
    age = int(age)

    if age < 3:
        print (f"The person's age is {age} so the ticket is free.")
    elif age < 12:
        print (f"The person's age is {age} so the ticket costs $10.")
    else:
        print (f"The person's age is {age} so the ticket costs $12.")
