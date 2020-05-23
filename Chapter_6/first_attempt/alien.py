# Making a list of aliens
aliens = []

# Make 30 green aliens
for alien_number in range(30):
    new_alien = {'colour': 'green', 'points': 5, 'speed': 'slow'}
    aliens.append(new_alien)

# Making yellow aliens
for alien in aliens[:3]:
    if alien ['colour'] == 'green':
        alien['colour'] = 'yellow' 
        alien['points'] = 10
        alien['speed'] = 'medium'

# Showing the first 5 aliens
for alien in aliens[:5]:
    print (alien)
print ("...")

# show how many aliens have been created
print (f"total number of aliens: {len(aliens)}")