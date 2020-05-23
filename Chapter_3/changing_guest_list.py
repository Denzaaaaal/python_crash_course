guests = ['cheryl', 'laverne', 'linval']

print (f"Hi {guests[0].title()}, I would like to invite you to dinner.")
print (f"Hi {guests[1].title()}, I would like to invite you to dinner.")
print (f"Hi {guests[2].title()}, I would like to invite you to dinner.")

print (f"It appears that {guests[2].title()} cannot make it.")
del guests[2]
guests.append('paul')

print (f"Hi {guests[0].title()}, I would like to invite you to dinner.")
print (f"Hi {guests[1].title()}, I would like to invite you to dinner.")
print (f"Hi {guests[2].title()}, I would like to invite you to dinner.")