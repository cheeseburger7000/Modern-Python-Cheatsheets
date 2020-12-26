age = 18
if age >= 18:
    print('You are old enough to vote!')
    print('Have you registered to vote yet?')

age = 17
if age >= 18:
    print('You are old enough to vote!')
    print('Have you registered to vote yet?')
else:
    print('Sorry, you are too young to vote.')
    print('Please register to vote as soon as you turn 18!')

age = 63
if age < 4:
    price = 0
elif age < 18:
    price = 5
elif age < 65:
    price = 10
else:
    price = 5
print('Your admission cost is $' + str(price) + '.')

requested_toppings = ['mushrooms', 'extra cheese']
if 'mushrooms' in requested_toppings:
    print('Adding mushrooms.')
if 'pepperoni' in requested_toppings:
    print('Adding pepperoni.')
if 'extra cheese' in requested_toppings:
    print('Adding extra cheese.')
print('\nFinished making your pizza!')

# Practice
alien_color = 'green'
if alien_color == 'yellow':
    print('You earned 5 points.')
else:
    pass
    # fails will have no output.

alien_color = 'yellow'
if alien_color == 'green':
    print('Your just earned 5 points for shooting the alien.')
else:
    print('Your just earned 10 points.')

alien_color = 'red'
if alien_color == 'green':
    points = 5
elif alien_color == 'yellow':
    points = 10
elif alien_color == 'red':
    points = 15
else:
    points = 0
print('Your earned ' + str(points) +' points for shooting ' + alien_color + ' alien.')

age = 22
if age < 2:
    print('Baby')
elif age >= 2 and age < 4:
    print('Toddler')
elif age >=4 and age < 13:
    print('Kid')
elif age >= 13 and age < 20:
    print('Teenager')
elif age >= 20 and age < 65:
    print('Adult')
elif age >= 65:
    print('Elder')
else:
    pass

favorite_fruits = ['🍌', '🍎', '🍊']
if '🍌' in favorite_fruits:
    print('You really like 🍌!')
if '💩' not in favorite_fruits:
    print('You not like 💩!')