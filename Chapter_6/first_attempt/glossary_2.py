glossary = {
    'slice': 'Used when calcuating the range of something. Mainly used the address the start, end and itteration',
    'list comprehension': 'A for loop in a list',
    'list': 'Several .entries formatted in a list',
    'dictionary': 'a list with key value pairs',
    'for_loop':' allows you to calculate something for a certain length of time',
    'set': 'a list that does not show duplicates. It uses the same brackets as a dictionary'
}

for word, definition in glossary.items():
    print (f"{word.title()}, {definition}")