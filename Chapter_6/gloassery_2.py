glossary = {
    'slice': 'a method for getting the the certain positon of something',
    'dictionary': 'a method for storing a key associated with a value',
    'tupple': 'a unchangable list',
    'list': 'a method of storing a certain ammount of items',
    'float': 'a decimal place number',
    'set': 'a list of unique values'
}

for word, definition in glossary.items():
    word = word.title()
    print (f"{word}, {definition}")