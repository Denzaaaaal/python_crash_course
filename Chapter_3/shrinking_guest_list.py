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

print ("\nIt appears that the new table will not arrive on time")

cancelled_guest = guests.pop(0)
print(f"\nSorry {cancelled_guest.title()}, It appears that I will have to retract my offer.")
cancelled_guest = guests.pop(0)
print(f"Sorry {cancelled_guest.title()}, It appears that I will have to retract my offer.")
cancelled_guest = guests.pop(2)
print(f"Sorry {cancelled_guest.title()}, It appears that I will have to retract my offer.")
cancelled_guest = guests.pop(2)
print(f"Sorry {cancelled_guest.title()}, It appears that I will have to retract my offer.")

print (f"\nHey {guests[0].title()}, you are still invited to my dinner.")
print (f"Hey {guests[1].title()}, you are still invited to my dinner.")
del guests[0]
del guests[0]
print (guests)