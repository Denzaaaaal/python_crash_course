pizzas = ['pepperoni', 'meatfeast', 'hot & spicy']
friends_pizzas = pizzas[:]

pizzas.append('bbq Chicken')
friends_pizzas.append('margharita')

for pizza in pizzas:
    print (f"One of my favorite pizza flavours is {pizza}")

for friends_pizza in friends_pizzas:
    print (f"My friends favorite pizza flavours is {friends_pizza}")