numbers = [value for value in range (1,10)]
for number in numbers:
    if number == 2:
        print (f"{number}nd")
    elif number == 3:
        print (f"{number}rd")
    else:
        print (f"{number}th")