# Moving item from one list to another
uncomfirmed_users = ['allen', 'james', 'jordan']
confirmed_users = []
while uncomfirmed_users:
    current_user = uncomfirmed_users.pop()
    print('Verifying user: ' + current_user.title())
    confirmed_users.append(current_user)
print('\nThe following users have been confirmed:')
for confirmed_user in confirmed_users:
    print(confirmed_user.title())

# Removing all instance of specific values from a list
users = ['allen', 'james', 'luca', 'jordan']
while 'luca' in users:
    users.remove('luca')
print(users)

# Filling in dictionary with user input
responses = {}
polling_active = True
while polling_active:
    name = input('What is your name? ')
    age = input('How old are you? ')
    responses[name] = age

    repeat = input('Should repeat? Y/N')
    if repeat == 'N':
        polling_active = False
for name, age in responses.items():
    print(name + ' age: ' + age)