# Input function accept string input
# msg = input('Tell me something, and i will repeat it back to you: ')
# print(msg)

# name = input('Please enter your name: ')
# print('Hello, ' + name + '!')

# prompt = 'If you tell us who you are, we can personalize the message you see.'
# prompt += '\nWhat is your first name? '
# name = input(prompt)
# print('Hello, ' + name + '!')

# Using int function to accept numerical input
# age = input('How old are you? ')
# print(int(age) > 18)

# height = input('How tall are you, in inches? ')
# height = int(height)
# if height >= 36:
#     print('\nYou\'re tall enough to ride!')
# else:
#     print('\nYou\'ll be able to ride when you\'re a litte older.')

# The module operator
number = input('Enter a number, and I\'ll tell you if it\'s even or odd: ')
number = int(number)
if number % 2 == 0:
    print('\nThe number ' + str(number) + ' is even.')
else:
    print('\nThe number ' + str(number) + ' is odd.')
