favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python'
}

poll_names = ['cheryl', 'denzel', 'jen', 'mark', 'edward','phil']

for poll_name in poll_names:
    if poll_name in favorite_languages.keys():
        print (f"Thank you {poll_name.title()} for taking our poll.")
    else:
        print (f"{poll_name.title()}, we have noticed that you have not taken a poll, please take one now.")