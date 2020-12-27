# Looping through all key-value pairs
user_0 = {
    'username': 'luca',
    'first': 'Yeung',
    'last': 'Shaohsiung'
}
for key, value in user_0.items():
    print('\nKey: ', key)
    print('Value: ', value)

favorite_languages = {
    'luca': 'java',
    'james': 'javascript',
    'allen': 'python'
}
for name, language in favorite_languages.items():
    print(name.title() + '\'s favorite language is ' + 
    language.title() + '.')

# Looping through all the keys in a dictionary
favorite_languages = {
    'luca': 'java',
    'james': 'javascript',
    'allen': 'python'
}
for name in favorite_languages.keys():
    print(name.title())

for name in favorite_languages:
    print(name.title())

friends = ['luca', 'michael', 'allen']
for name in favorite_languages:
    print(name.title())

    if name in friends:
        print('Hi ' + name.title() + 
            ', I see your favorite language is ' + 
            favorite_languages[name].title() + '!')

if 'erin' not in favorite_languages.keys():
    print('Erin, please take our poll!')

if 'erin' not in favorite_languages:
    print('Erin, please take our poll!')

# Looping through a dictionary's key in order
favorite_languages = {
    'luca': 'java',
    'james': 'javascript',
    'allen': 'python',
    'curry': 'c++'
}
for name in sorted(favorite_languages.keys()):
    print(name)

# Looping through all values in a dictionary
favorite_languages = {
    'luca': 'java',
    'james': 'javascript',
    'allen': 'python',
    'curry': 'c++',
    'bruce': 'python'
}
for value in favorite_languages.values():
    print(value.title())
# checking for repeats
for value in set(favorite_languages.values()):
    print(value.title())