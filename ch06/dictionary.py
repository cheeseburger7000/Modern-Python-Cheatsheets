alien_0 = { "color": "green", 'points': 5 }
print(alien_0['color'])
print(alien_0['points'])

alien_0 = { 'color': 'green', 'points': 5 }
new_points = alien_0['points']
print('You just earned ' + str(new_points) + ' points!')

alien_0 = { 'color': 'green', 'points': 5 }
print(alien_0)
alien_0['x_position'] = 0
alien_0['y_position'] = 25
print(alien_0)

alien_0 = {}
alien_0['color'] = 'yellow'
alien_0['points'] = 10
print(alien_0)

# Modifying Values in a dictionary
alien_0 = { 'color': 'green' }
print('alien_0 color is ', alien_0['color'])
alien_0['color'] = 'yellow'
print('alien_0 color now is ', alien_0['color'])

# anthor example for modifying
alien_0 = { 'color': 'green', 'x_position': 0, 'y_position': 25, 'speed': 'medium' }
X_KEY = 'x_position'
print('Originial x_position: ', alien_0[X_KEY])
if alien_0['speed'] == 'slow':
    x_increment = 1
elif alien_0['speed'] == 'medium':
    x_increment = 2
else:
    x_increment = 3
alien_0[X_KEY] = alien_0[X_KEY] + x_increment
print('New x-position: ', alien_0[X_KEY])

# Remoing key-value pairs
alien_0 = { 'color': 'green', 'points': 5 }
del alien_0['color']
print(alien_0)

# A dictionary of similar Objects
favorite_languages = {
    'luca': 'java',
    'allen': 'python',
    'bruce': 'go',
}
person = 'luca'
print(person + '\'s favorite language is ' +
    favorite_languages[person].title() +
    '.')


# Practice - Person
person = {
    'first_name': 'Yeung',
    'last_name': 'Shaohsiung',
    'age': 22,
    'city': 'Taipei'
}
print('name: ', person['first_name'] + ' ' + person['last_name'])
print('city: ', person['city'])
print('age: ', person['age'])