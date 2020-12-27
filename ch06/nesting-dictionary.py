# A list of dictionaries
alien_0 = { 'color': 'green', 'points': 5 }
alien_1 = { 'color': 'yellow', 'points': 10 }
alien_2 = { 'color': 'red', 'points': 15 }
aliens = [alien_0, alien_1, alien_2]
for alien in aliens:
    print(alien)

aliens = []
for idx in range(0, 30):
    new_alien = { 'color': 'green', 'points': 5, 'speed': 'slow' }
    aliens.append(new_alien)
for alien in aliens[:3]:
    if alien['color'] == 'green':
        alien['color'] = 'yellow'
        alien['speed'] = 'medium'
        alien['points'] = 10
    elif alien['color'] == 'yellow':
        alien['color'] = 'red'
        alien['speed'] = 'fast'
        alien['points'] = 15
    else:
        pass
for alien in aliens[:5]:
    print(alien)
print('...')
total_alien_numbers = len(aliens)
print('Total number of aliens: ', str(total_alien_numbers))

# A list in a dictionary
pizza = {
    'crust': 'thick',
    'toppings': [
        'mushrooms',
        'extra cheese'
    ],
}
print('You ordered a ' + 
    pizza['crust'] +
    '-crust pizza ' + 
    'with the following toppings:')
for topping in pizza['toppings']:
    print('\t' + topping)

favorite_languages = {
    'luca': ['python', 'ruby'],
    'bruce': ['java', 'javascript'],
    'james': ['go']
}
for name, languages in favorite_languages.items():
    if len(languages) > 1:
        print('\n' + name.title() + '\'s favorite languages are:')
    elif len(languages) == 1:
        print('\n' + name.title() + '\'s favorite language is:')
    else:
        pass
    for language in languages:
        print('\t' + language.title())

# a dictionary in a dictionary
users = {
    'luca': {
        'first': 'yeung',
        'last': 'shaohsiung',
        'location': 'texas'
    },
    'allen': {
        'first': 'allen',
        'last': 'iverson',
        'location': 'taipei'
    }
}
for username, user_info in users.items():
    print('\nUsernameL: ', username)
    full_name = user_info['first'] + ' ' + user_info['last']
    location = user_info['location']
    print('\tFull name: ', full_name.title())
    print('\tLocation: ', location.title())