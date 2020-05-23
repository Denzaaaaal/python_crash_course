vacation = {}

survey = True
while survey == True:
    name = input("Enter your name: ")
    location = input(f"{name.title()}, if you could visit one place in the world, where would you go? ")
    vacation[name] = location
    print (f"Thanks {name.title()} for taking the survey")

    # Creating the end of the program
    survey_again = input("\nWould you like to do the survey again: (yes/no) ")
    survey_again = survey_again.lower()
    if survey_again != 'yes':
        print ("The results of the survey are :")
        for name, location in vacation.items():
            print (f"{name.title()} would like to go to {location.title()}.")
        break
