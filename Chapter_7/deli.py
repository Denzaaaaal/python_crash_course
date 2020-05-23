sandwitch_orders = ['ham and cheese', 'bacon', 'tuna']
finsished_sandwitches = []

while sandwitch_orders:
    sandwitch = sandwitch_orders.pop()
    print (f"I made your {sandwitch} sandwitch!")
    finsished_sandwitches.append(sandwitch)

print ("\nThe sandwitches that was made was: ")
for sandwitch in finsished_sandwitches:
    print (f"{sandwitch.title()} Sandwitch")