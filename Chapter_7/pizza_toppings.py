prompt = "Please enter in a Pizza Topping: "
prompt += "\n(Enter in 'quit' when you want to exit) "

active = True
while active == True:
    topping = input(prompt)
    
    if topping == 'quit':
        break

    print (f"added {topping} to your pizza.")