# Checking for special items
request_toppings = ['mushrooms', 'green peppers', 'extra cheese']
for request_topping in request_toppings:
    if request_topping == 'green peppers':
        print('Sorry, we are out of green peppers right now.')
    else:
        print('Adding ' + request_topping + '.')
print('\nFinished making your pizza!')

# Checking that a list is not empty
request_toppings = []
if request_toppings: # an empty list evaluates to False [IMPORTANT]
    for request_topping in request_toppings:
        print('Adding ' + request_topping + '.')
    print('/nFinished making your pizza!')
else:
    print('Are you sure you are want a plain pizza?')

# Using multiple list
available_toppings = ('mushrooms', 'olives', 'green peppers', 
    'pepperoni', 'pineapple', 'extra cheese')
request_toppings = ['mushrooms', 'french fries', 'extra cheese']
for request_topping in request_toppings:
    if request_topping in available_toppings:
        print('Adding ' + request_topping + '.')
    else:
        print('Sorry, we don\'t have ' + request_topping + '.')
print('\nFinished making your pizza!')


# Practice - Hello Admin
username = 'admin'
# sys_usernames = ['admin', 'luca', 'allen']
sys_usernames = []
if not sys_usernames: # 集合为空取反
    print('We need to find some users!')
elif username not in sys_usernames:
    print('You are not register yet.')
elif username in sys_usernames and username.lower() == 'admin':
    print('Hello admin, would you like to see a status report¿')
else:
    print('Hello ' + username + ', thank you for logging in again.')


# Practice - Checking usernames
new_users = ['luca', 'ALLEN', 'bruce']
current_users = ['LUCA', 'michael', 'allen']
for new_user in new_users:
    if (new_user.lower() in current_users) or (new_user.upper() in current_users):
        print('Username ' + new_user + ' has been used, you need to enter a new username.')
    else:
        print('Username ' + new_user + ' is available.')

# Practice - Ordinal numbers
ordinal_numbers = list(range(1, 10))
for ordinal_number in ordinal_numbers:
    if ordinal_number == 1:
        print(str(ordinal_number) + 'st')
    elif ordinal_number == 2:
        print(str(ordinal_number) + 'nd')
    elif ordinal_number > 2 and ordinal_number < 10:
        print(str(ordinal_number) + 'th') 
    else:
        pass

# last but not least, conditional tests is important.
# Consider games you might want to write, 
# data sets you might want to explore, 
# and web applications you’d like to create.