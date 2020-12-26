message = 'Hello Python'
print(message)

message = 'Hello Python Crash Course'
print(message)

# Python 命名规范
#
# 1. Letters, numbers and underscores. 
# Start with a letter or underscore, but not with a number.
#
# 2. Cannot use spaces to separate words in variable names, using underscores.
#
# 3. Don't using Python keywords and build-in function names as variable names.
#
# 4. Variable names should be short and descriptive.
#
# 5. Lowercase letter l and uppercase letter O could be confused with the number 1 and 0.
#
# 如何练习命名？
# 多写代码、多读别人写的代码。

# String
# 1.Dealing with case
name = 'hOw to build a weB aPPlication'
print(name.title())

print(name.upper())
print(name.lower()) # Convert strings to lowercase before storing them.

# 2.Concatenation
first_name = 'yeung'
last_name = 'shaohsiung'
full_name = first_name + ' ' + last_name
print(full_name)

print('Hello, ' + full_name.title() + '!')

message = 'Hello, ' + full_name.title() + '!'
print(message)

# 3.Newlines and tabs
print('Python')
print('\tPython')
print('Python\nJava\nGo')
print('Languages:\n\tPython\n\tJava\n\tGo')

# 4.Stripping whitespace
# Whitespace: spaces, tabs, and end-of-line symbols.
favorite_language = ' python '
print(favorite_language.rstrip()) # immutable
print(favorite_language.lstrip())
print(favorite_language.strip())

# Practice
famous_person = 'Alert Einstein'
message = famous_person + '''once said, "A person who never made a 
mistake never tried anything new."'''
print(message)

player_name = 'Michael Jordan'
partner_name = 'Kobe Bryant'
print('\t' + player_name + '\t' + partner_name + '\n\t' + player_name + '\t' + partner_name)

