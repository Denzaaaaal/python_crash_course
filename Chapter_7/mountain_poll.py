responses = {}

# Set a flag to indicate the poll is active
poll_active = True

while poll_active:
    # prompt for persons name and response
    name = input("\nWhat is your name? ")
    response =  input ("Which mountain would you like to climb someday? ")

    # Store response in a dictionary
    responses[name] = response

    # Find out if anyone else is going to take the poll
    repeat = input("Would you like to let another person respond? (yes/no) ")
    if repeat == 'no':
        poll_active = False

print ("\n--- Poll Results ---")
for name, response in responses.items():
    print (f"{name} would you like to climb {response}")
