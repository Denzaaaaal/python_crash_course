# Making a list of aliens
aliens = []

# Making 30 green aliens
for alien_number in range (30):
    new_alien = {'colour': 'green', 'points': 5, 'speed': 'slow'}
    aliens.append(new_alien)

# Making the first 5 aliens fast
for alien in aliens[:3]:
    if alien['colour'] == 'green':
        alien['colour'] = 'yellow'
        alien['speed'] = 'medium'
        alien['points'] = 10

# Show the first 5 aliens
for alien in aliens[:5]:
    print(alien)
print ("...")

# Show how many aliens have been created.
print (f"Total ammount of aliens created {len(aliens)}")