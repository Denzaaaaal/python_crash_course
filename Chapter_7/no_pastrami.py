sandwitch_orders = ['ham and cheese', 'pastrami','bacon','pastrami', 'tuna','pastrami']
finsished_sandwitches = []

while sandwitch_orders:
    if sandwitch_orders[-1] == 'pastrami':
        print ("The deli has run out of pastrami")
        del sandwitch_orders[-1]
    sandwitch = sandwitch_orders.pop()
    print (f"I made your {sandwitch} sandwitch!")
    finsished_sandwitches.append(sandwitch)

print ("\nThe sandwitches that was made was: ")
for sandwitch in finsished_sandwitches:
    print (f"{sandwitch.title()} Sandwitch")