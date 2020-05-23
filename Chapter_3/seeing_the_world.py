destinations = ['jamaica', 'america', 'japan', 'south korea', 'nigeria']
print ("Here is the original order:")
print (destinations)

print ("here is the sorted order: ")
print (sorted(destinations))
print ("Here is the original order:")
print (destinations)
print ("Here is the sorted reverse order: ")
print (sorted(destinations, reverse=True))
print ("Here is the original list again: ")
print (destinations)

destinations.reverse()
print ("Here is the list reversed perminantly: ")
print (destinations)

destinations.reverse()
print ("here is the list reveresed back to the original order:")
print (destinations)

destinations.sort()
print ("Here is the list sorted in alphabetical order:")
print (destinations)

destinations.sort(reverse=True)
print ("Here is the list sorted in reverse alphabetical order:")
print (destinations)