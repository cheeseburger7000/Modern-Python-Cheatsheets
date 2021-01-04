# Python Grammer Cheatsheets

## While

```py
cur = 1
while cur < 3:
    print(cur)
    cur += 1
    
'''
Output:
1
2
'''
```

## While-Else 

```py
cur = 1
while cur < 3:
    print(cur)
    cur += 1
else:
    print('else block output: ' + str(cur))

'''
Output:
1
2
else block output: 3
'''
```

## While with Break and Continue

```py
cur = 1
while True:
    if cur > 3:
        break
    print(cur)
    cur += 1

'''
Output:
1
2
3
'''
```

# Function

## Declare/Call/Parameters/Return Value

```py
def getName(first_name, last_name):
	full_name = first_name + ' ' + last_name
	return full_name

getName('Shaohsiung', 'Yeung')
```

## K-V Arguments

```py
def getName(first_name, last_name):
	full_name = first_name + ' ' + last_name
	return full_name

getName(first_name='Shaohsiung', last_name='Yeung')
getName(last_name='Yeung', first_name='Shaohsiung')
```

## Default Value of Parameters

```py
def getName(first_name, last_name, middle_name = ''):
	if middle_name:
		full_name = first_name + ' ' + middle_name + ' ' + last_name
	else:
		full_name = first_name + ' ' + last_name
	return full_name

getName('Shaohsiung', 'Yeung')
getName('Shaohsiung', 'Yeung', 'J')
```

## Arbitrary Number of Arguments

```py
def order_pizza(inch, *toppings):
	print(f'You order {inch}-inch pizza, toppings are:')
	print(toppings) # toppings is a tuple
	for topping in toppings:
		print(f'- {topping}')

order_pizza(18, 'egg', 'pepper', 'cheese')
```

## Arbitrary Keyword Arguments

```py
def printUserInfo(user_id, **user_info):
	print(f'user id: {user_id}')
	for k, v in user_info.items(): # user_info is a dict
		print(f'{k}: {v}')

printUserInfo(7, user_name='luca', age=22)
```

## Callback Function

```py
def outputNameByHandler(handler, name):
	upper_name = name.title()
	return handler(upper_name)

def standardNameHandler(name):
	return f'Your name is {name}.'

def htmlNameHandler(name):
	return f'<h2>Your name is {name}.</h2>'

name = 'luca'
print(outputNameByHandler(htmlNameHandler, name))
print(outputNameByHandler(standardNameHandler, name))
```

# Module

## Import Functions from Module

Creating a person Module, includes function: `printName` and `printAge`.

```py 
# person.py
def printName(name):
	print(f'Name is {name.title()}.')

def printAge(age):
	print(f'Age is {age}.')

def printAddress(address):
	print(f'Address is {address.title()}.')
```

You can use `import` keyword to import all content.

```py
# main.py
import person

person.printName('luca')
person.printAge(22)
```

Or you can use `from Module import Function` keyword to import specified function like this.

```py
from person import printName, printAge

printName('luca')
printAge(22)
```

## Import Classes from Modlue

Create a class Person inside person module.

```py
# person.py
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def info(self):
        print(f'My name is {self.name.title()}, age is {self.age}.')
```

Use `import` keyword import all content.

```py
import person

p = person.Person('luca', 22)
p.info()
```

Or you can use `from Module import Class` import specified class.

```py
# main.py
from person import Person 

p = Person('luca', 22)
p.info()
```

## Alias Module

Rename the name of the module.

```py
import person as p

p.printName()
```

Rename the name of the specified class or function.

```py
from person import printName as pName, Person as p

# function
name = 'luca'
pName(name)

# class
luca = p(name, 22)
luca.info()
```

## Build-in Modules


### OS Module

```py
import os

path = 'new_directory'
os.mkdir(path)
os.chdir(path)
print(os.getcwd())
os.rmdir(path)
```

### Sys Module

```py
import sys

# Get the argument passed from the command line.
print(f'Welcome {sys.argv[1]}. Enjoy {sys.argv[2]} challenge!')
```

### Statistics Module

todo

### Math Module

todo

### String Module

```py
import string

print(string.ascii_letters) # abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ
print(string.digits)        # 0123456789
print(string.punctuation)   # !"#$%&'()*+,-./:;<=>?@[\]^_`{|}~
```

### Random Module

```py
from random import random, randint

print(random()) # returns a value between 0 and 0.9999
print(randint(5, 20)) # returns a random integer number between 5 and 20
```
