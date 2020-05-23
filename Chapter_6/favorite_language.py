favorite_languages = {
    'jen': ['python', 'ruby'],
    'sarah': ['c'],
    'edward': ['ruby','go'],
    'phil': ['python', 'go'],
}

print ("The following languages have been mentioned:")
for name, languages in favorite_languages.items():
    if len(languages) > 1:
        print (f"\nMy name is {name.title()} and my favorite languages are:")
    else: 
        print (f"\nMy name is {name.title()} and my favorite language is: ")
    for language in languages:
        print (language.title())