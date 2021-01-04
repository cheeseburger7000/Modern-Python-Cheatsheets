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
    print(cur)

'''
Output:
1
2
3
'''
```

## While with Break

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
