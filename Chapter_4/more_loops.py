my_foods = ['pizza','falafel','carrot cake']
friends_foods = my_foods [:]

my_foods.append('rice')
friends_foods.append('ice cream')

for food in my_foods:
    print(f"One of my favorite foods is {food}.")

for friends_food in friends_foods:
    print (f"One of my friends favorite foods is {friends_food}.")