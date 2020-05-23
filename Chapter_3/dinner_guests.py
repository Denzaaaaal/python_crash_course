guests = ['cheryl', 'laverne', 'linval']

print (f"Hi {guests[0].title()}, I would like to invite you to dinner.")
print (f"Hi {guests[1].title()}, I would like to invite you to dinner.")
print (f"Hi {guests[2].title()}, I would like to invite you to dinner.")

print (f"\nIt appears that {guests[2].title()} cannot make it.")
del guests[2]
guests.append('paul')

print (f"\nHi {guests[0].title()}, I would like to invite you to dinner.")
print (f"Hi {guests[1].title()}, I would like to invite you to dinner.")
print (f"Hi {guests[2].title()}, I would like to invite you to dinner.")

print ("\nIt appears that I have found a bigger table")
# adding 3 more people (list now totals at 6)
guests.insert(0, 'shaunee')
guests.insert(1, 'cathy')
guests.append('thenuja')

print (f"\nHi {guests[0].title()}, I would like to invite you to dinner")
print (f"Hi {guests[1].title()}, I would like to invite you to dinner.")
print (f"Hi {guests[2].title()}, I would like to invite you to dinner.")
print (f"Hi {guests[3].title()}, I would like to invite you to dinner.")
print (f"Hi {guests[4].title()}, I would like to invite you to dinner.")
print (f"Hi {guests[5].title()}, I would like to invite you to dinner.")

print (f"\nThe amount of guests comming to this dinner is {len(guests)}.")