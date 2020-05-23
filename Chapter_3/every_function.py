languages = ['spanish', 'french', 'english','japanese', 'korean']

languages.append('german')
print ("\nAdding to the list:")
print (languages)

languages.remove('german')
print("\nRemoving from the list:")
print (languages)

print("\nTemporarly sorting the list:")
print (sorted(languages))

print ("\nTHe original list:")
print (languages)

print("\nThe list sorted in reverse")
print(sorted(languages, reverse=True))

print ("\nselecting and entry in the list:")
print (languages[0])


print ("\npoped entry of a list:")
popped_language = languages.pop(1)
print (popped_language)

print ("\ndeleting from the list:")
del languages[1]
print (languages)

print ("\nremoving from the list:")
languages.remove('korean')
print (languages)

print ("adding to the list in a specific place")
languages.insert(1, 'arabic')
print (languages)

languages.sort()
print ("\nSorting the list:")
print (languages)

languages.sort(reverse=True)
print ("\nSorting the list in reverse order")
print (languages)

languages.reverse()
print ("\nPrinting the list in the reverse order:")
print (languages)

print ("\nwhat is the length of the list:")
print(len(languages))