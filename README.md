# Modern Python Cheatsheets

## Table of Contents

- [While](#while)
    - [While-Else](#while-else)
    - [While with Break and Continue](#while-with-break-and-continue)
- [Function](#function)
    - [Declare/Call/Parameters/Return Value](#declare/call/parameters/return-value)
    - [K-V Arguments](#k-v-arguments)
    - [Default Value of Parameters](#default-value-of-parameters)
    - [Arbitrary Number of Arguments](#arbitrary-number-of-arguments)
    - [Arbitrary Keyword Arguments](#arbitrary-keyword-arguments)
    - [Callback Function](#callback-function)
- [Module](#module)
    - [Import Functions from Module](#import-functions-from-module)
    - [Import Classes from Modlue](#import-classes-from-modlue)
    - [Alias Module](#alias-module)
    - [Build-in Modules](#build-in-modules)
- [List Comprehension](#list-comprehension)
    - [Change a string to a list of characters](#change-a-string-to-a-list-of-characters)
    - [Generate a list of numbers](#generate-a-list-of-numbers)
    - [Combined with if expression](#combined-with-if-expression)
- [Lambda Function](#lambda-function)
    - [Self invoking lambda function](#self-invoking-lambda-function)
    - [Lambda Function Inside Another Function](#lambda-function-inside-another-function)
- [Higher Order Functions](#higher-order-functions)
    - [Function as a Parameter](#function-as-a-parameter)
    - [Function as a Return Value](#-function-as-a-return-value)
    - [Closures](#closures)
    - [Decorators](#decorators)
    - [Built-in Higher Order Functions](#built-in-higher-order-functions)
- [Python Error Types](#python-error-types)    
    - [SyntaxError](#syntaxerror)
    - [NameError](#nameerror)
    - [IndexError](#indexError)
    - [ModuleNotFoundError](#modulenotfounderror)
    - [AttributeError](#attributeerror)
    - [KeyError](#keyerror)
    - [TypeError](#typeerror)
    - [ImportError](#importerror)
    - [ValueError](#valueerror)
    - [ZeroDivisionError](#zerodivisionerror)
- [try-except-else-finally](#try-except-else-finally)
- [Collection Related Operations](#collection-related-operations)
    - [Unpacking Lists](#unpacking-lists)
    - [Unpacking Dictionaries](#unpacking-dictionaries)
    - [Packing Lists](#packing-lists)
    - [Packing Dictionaries](#packing-dictionaries)
    - [Spreading](#spreading)
    - [Enumerate](#enumerate)
    - [Zip](#zip)
- [File Handling](#file-handling)
    - [Opening Files for Reading](#opening-files-for-reading)
    - [Using with to close file automatically](#using-with-to-close-file-automatically)
    - [Opening Files for Overwrite or Append](#opening-files-for-aoverwrite-or-append)
    - [Deleting Files](#deleting-files)
- [File Types](#file-types)
    - [json](#json)
    - [csv](#csv)
    - [xlsx](#xlsx)
    - [xml](#xml)
- [PIP](#pip)
    - [Package](#package)
- [todo](#todo)

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

### While-Else 

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

### While with Break and Continue

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

**[⬆ Back to Top](#table-of-contents)**

## Function

### Declare/Call/Parameters/Return Value

```py
def getName(first_name, last_name):
	full_name = first_name + ' ' + last_name
	return full_name

getName('Shaohsiung', 'Yeung')
```

### K-V Arguments

```py
def getName(first_name, last_name):
	full_name = first_name + ' ' + last_name
	return full_name

getName(first_name='Shaohsiung', last_name='Yeung')
getName(last_name='Yeung', first_name='Shaohsiung')
```

### Default Value of Parameters

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

### Arbitrary Number of Arguments

```py
def order_pizza(inch, *toppings):
	print(f'You order {inch}-inch pizza, toppings are:')
	print(toppings) # toppings is a tuple
	for topping in toppings:
		print(f'- {topping}')

order_pizza(18, 'egg', 'pepper', 'cheese')
```

### Arbitrary Keyword Arguments

```py
def printUserInfo(user_id, **user_info):
	print(f'user id: {user_id}')
	for k, v in user_info.items(): # user_info is a dict
		print(f'{k}: {v}')

printUserInfo(7, user_name='luca', age=22)
```

**[⬆ Back to Top](#table-of-contents)**

### Callback Function

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

**[⬆ Back to Top](#table-of-contents)**

## Module

### Import Functions from Module

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

### Import Classes from Modlue

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

### Alias Module

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

### Build-in Modules


#### OS Module

```py
import os

path = 'new_directory'
os.mkdir(path)
os.chdir(path)
print(os.getcwd())
os.rmdir(path)
```

#### Sys Module

```py
import sys

# Get the argument passed from the command line.
print(f'Welcome {sys.argv[1]}. Enjoy {sys.argv[2]} challenge!')
```

#### Statistics Module

todo

#### Math Module

todo

#### String Module

```py
import string

print(string.ascii_letters) # abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ
print(string.digits)        # 0123456789
print(string.punctuation)   # !"#$%&'()*+,-./:;<=>?@[\]^_`{|}~
```

#### Random Module

```py
from random import random, randint

print(random()) # returns a value between 0 and 0.9999
print(randint(5, 20)) # returns a random integer number between 5 and 20
```

**[⬆ Back to Top](#table-of-contents)**

## List Comprehension

A faster, short way to create a new list from a sequence then using the for loop. Syntax: `[i for i in iterable if expression]`

### Change a string to a list of characters

```py
language = 'React'
lst = [ch for ch in language]
print(lst) # ['R', 'e', 'a', 'c', 't']
```

### Generate a list of numbers

```py
lst = [n for n in range(0, 5)]
print(lst) # 0 1 2 3 4
```

### Combined with if expression

```py
even_numbers = [n for n in range(0, 10) if n % 2 == 0]
print(even_numbers) # [0, 2, 4, 6, 8]
```

**[⬆ Back to Top](#table-of-contents)**

## Lambda Function 

Lambda function is a small anonymous function without a name. Syntax: `x = lambda param1, param2: param1 + param2`, execute `x(arg1, arg2)`.

```py
add_two_nums = lambda a, b: a + b
result = add_two_nums(2,3)
print(result) # 5
```

### Self invoking lambda function

```py
result = (lambda a, b: a + b)(2,3)
print(result) # 5
```

### Lambda Function Inside Another Function

```py
def power(x):
    return lambda n : x ** n

cube = power(2)(3)
print(cube) # 8
```

**[⬆ Back to Top](#table-of-contents)**

## Higher Order Functions

### Function as a Parameter

todo

### Function as a Return Value

todo

### Closures

Python allows a nested function to access the outer scope of the enclosing function. This is is known as a Closure(闭包).

```py
def add_ten():
    ten = 10

    def add(num):
        return num + ten
    return add

closure_result = add_ten()
print(closure_result(5))  # 15
print(closure_result(10))  # 20
```

### Decorators

A decorator is a design pattern in Python that allows a user to add new functionality to an existing object without modifying its structure.(AOP)

```py
def title_list(function):
    def wrapper():
        result = []
        items = function()
        for item in items:
            result.append(item.title())
        return result
    return wrapper


def html_li_tag(function):
    def wrapper():
        result = ''
        items = function()
        for item in items:
            result += f'<li>{item}</li>'
        return result
    return wrapper


def html_ul_tag(function):
    def wrapper():
        lis = function()
        return f'<ul>{lis}</ul>'
    return wrapper


@html_ul_tag
@html_li_tag
@title_list
def todo_items():
    return ['read book', 'watch show', 'cook']


def output_html_todo_list():
	print(todo_items())


output_html_todo_list()

'''
Output:
<ul><li>Read Book</li><li>Watch Show</li><li>Cook</li></ul>
'''
```

### Built-in Higher Order Functions

#### map

```py
lst = [n for n in range(0, 5)]
result = map(lambda x: x * 3, lst)
print(list(result))
```

#### filter

```py
lst = [n for n in range(0, 5)]
result = filter(lambda x: x % 2 == 0, lst)
print(list(result))
```

#### reduce

```py
from functools import reduce

lst = [n for n in range(1, 5)]
result = reduce(lambda x, y: x + y, lst) # 10
result = reduce(lambda x, y: x * y, lst) # 24
```

**[⬆ Back to Top](#table-of-contents)**

## Python Error Types

### SyntaxError

```py
print 'halo'
# SyntaxError: Missing parentheses in call to 'print'. Did you mean print('halo')?


print('halo')
'''
Output:
halo
'''
```

### NameError

```py
print(age)
# NameError: name 'age' is not defined


age = 22
print(age)
'''
Output:
22
'''
```

### IndexError

```py
numbers = [1, 2, 3, 4, 5]
numbers[5]
# IndexError: list index out of range
```

### ModuleNotFoundError

```py
import maths
# ModuleNotFoundError: No module named 'maths'


import math
```

### AttributeError

```py
import math
print(math.PI)
# AttributeError: module 'math' has no attribute 'PI'


print(math.pi)
# 3.141592653589793
```

### KeyError

```py
users = {'name':'Asab', 'age':250, 'country':'Finland'}
users['county']
# KeyError: 'county'


users['country']
# Finland
```

### TypeError

```py
4 + '3'
# TypeError: unsupported operand type(s) for +: 'int' and 'str'


4 + int('3')
# 7
4 + float('3')
# 7.0
```

### ImportError

```py
from math import power
# ImportError: cannot import name 'power' from 'math'


from math import pow
pow(2,3)
# 8.0
```

### ValueError

```py
int('12a')
# ValueError: invalid literal for int() with base 10: '12a'
```

### ZeroDivisionError

```py
1/0
# ZeroDivisionError: division by zero
```

**[⬆ Back to Top](#table-of-contents)**

## try-except-else-finally

```py
n = input('Please input a number: ')
try:
    result = 1/int(n)
except ZeroDivisionError:
    print('You cannot do 1/0')
except ValueError:
    print('illegal value: ', n)
else:
    print('result: ' + str(result))
finally:
    print('exit')
```

**[⬆ Back to Top](#table-of-contents)**

## Collection Related Operations

### Unpacking Lists

```py
def sum_of_five_nums(a, b, c, d, e):
    return a + b + c + d + e

lst = [1, 2, 3, 4, 5]
print(sum_of_five_nums(*lst))  # 15
```

Unpacking lists for varilable.

```py
countries = ['Finland', 'Sweden', 'Norway', 'Denmark', 'Iceland']
fin, sw, nor, *rest = countries
print(fin, sw, nor, rest)   # Finland Sweden Norway ['Denmark', 'Iceland']


numbers = [1, 2, 3, 4, 5, 6, 7]
one, *middle, last = numbers
print(one, middle, last)      #  1 [2, 3, 4, 5, 6] 7
```

### Unpacking Dictionaries

```py
def unpacking_person_info(name, country, city, age):
    return '{name} lives in {country}, {city}. He is {age} year old.'

dct = {'name':'Asabeneh', 'country':'Finland', 'city':'Helsinki', 'age': 250}
print(unpacking_person_info(**dct)) # Asabeneh lives in Finland, Helsinki. He is 250 years old.
```

### Packing Lists

```py
def sum_all(*args):
    s = 0
    for i in args:
        s += i
    return s

      
print(sum_all(1, 2, 3, 4, 5, 6, 7))
```

### Packing Dictionaries

```py
def packing_person_info(**kwargs):
    # print(type(kwargs))
    for key in kwargs:
        print("{key} = {kwargs[key]}")
    return kwargs

print(packing_person_info(name="Asabeneh", country="Finland", city="Helsinki", age=250))
```

### Spreading

```py
lst_one = [1, 2, 3]
lst_two = [4, 5, 6,7]
lst = [0, *list_one, *list_two]
print(lst) # [0, 1, 2, 3, 4, 5, 6, 7]

country_lst_one = ['Finland', 'Sweden', 'Norway']
country_lst_two = ['Denmark', 'Iceland']
nordic_countries = [*country_lst_one, *country_lst_two]
print(nordic_countries) # ['Finland', 'Sweden', 'Norway', 'Denmark', 'Iceland']
```

### Enumerate

```py
for index, i in enumerate(countries):
    print('hi')
    if i == 'Finland':
        print('The country {i} has been found at index {index}')
```

### Zip

todo for Illustrating

```py
fruits = ['banana', 'orange', 'mango', 'lemon']                    
vegetables = ['Tomato', 'Potato', 'Cabbage','Onion', 'Carrot']
fruits_and_veges = []
for f, v in zip(fruits, vegetables):
    fruits_and_veges.append({'fruit':f, 'veg':v})

print(fruits_and_veges)
```

**[⬆ Back to Top](#table-of-contents)**

## File Handling

Syntax: `open('filename', model)`. Mode: r for read, a for append, w for write, x for create, t for text, b for binary.

### Opening Files for Reading

```py
f = open('words.txt') # default mode: rt
all_txt = f.read()
first_10_chars = f.read(10)
lines = f.readlines()
print(type(lines)) # lst
f.close()
```

### Using with to close file automatically

```py
with open('words.txt') as f:
    lines = f.read()
```

### Opening Files for Overwrite or Append 

Overwrite:

```py
with open('words.txt', 'w') as f:
    f.write('create a new file, if the file does not exists.')
```

Append:

```py
with open('words.txt', 'a') as f:
    f.write('will append to the end of the file, if the file does not exist it raise FileNotFoundError')
```

### Deleting Files

```py
import os 

if os.path.exist('words.txt'):
    os.remove('words.txt')
```

**[⬆ Back to Top](#table-of-contents)**

## File Types

### json

JSON to Dictionary

```py
import json

person_json = '''{
    "name": "luca",
    "country": "America",
    "city": "Texas",
    "skills": ["JavaScrip", "React", "Python", "Go", "Java"]
}'''

person_dict = json.loads(person_json)
print(person_dict['name'])
```

Dictionary to JSON

```py
import json

person = {
    "name": "luca",
    "country": "America",
    "city": "Texas",
    "skills": ["JavaScrip", "React", "Python", "Go", "Java"]
}

person_json = json.dumps(person, indent=4)
print(type(person_json)) # str
```

Saving as JSON File

```py
import json 

person = {
    "name": "luca",
    "country": "America",
    "city": "Texas",
    "skills": ["JavaScrip", "React", "Python", "Go", "Java"]
}
with open('person.json', 'w', encoding='utf-8') as f:
    json.dump(person, f, ensure_ascii=False, indent=4)
```

### csv

persons.csv

```csv
"name","country","city","skills"
"Luca","America","Texas","JavaScrip"
```

Reading csv file 

```py
import csv 

with open('persons.csv') as f:
    csv_reader = csv.readr(f, delimiter=',')
    for row in csv_reader:
        print(f'{row[0]}, {row[1]}, {row[2]}.')
```

### xlsx

todo xlrd

### xml

todo 

**[⬆ Back to Top](#table-of-contents)**

## PIP

We use pip to install different python packages. 

Package is a python module that can contain one or more modules or other packages. 

```bash
pip --version

pip install numpy

pip show numpy
pip show --verbose numpy

pip uninstall numpy

# See the installed packages on our machine
pip list

# Generate output suitable for a requirements file
pip freeze > requirements.txt
```

### Package

todo 

**[⬆ Back to Top](#table-of-contents)**

## todo

- [Python Style Guide](https://python-guide.gitbooks.io/python-style-guide/content/style-guide/code.html)