# Writing prompt
prompt = "Let's find out if a number is a multiple of 10"
prompt += "\nPlease enter a number: "

number = input(prompt)
number = int(number)

# Finding out if the number is divisable by 10
if number % 10 == 0:
    print (f"The number {number} is a multiple of 10")
else:
    print (f"The number {number} is not a multiple of 10")