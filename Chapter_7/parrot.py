prompt = "\nTell me something, and I will repeat it back to you"
prompt += "\nEner 'quit' to end the program. "

active = True
while active == True:
    message =input(prompt)
    
    if message == "quit":
        active = False
    else:
        print (message)