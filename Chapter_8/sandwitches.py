def toppings(*toppings):
    """ This prints all the items inside a sandwitch"""
    print ("\nMaking a sandwitch with the following items: ")
    for topping in toppings:
        print(f"- {topping.title()}")

toppings('strawberry jam', 'seaweed', 'rice', 'salmon')