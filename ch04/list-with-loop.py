magicians = ['alice', 'david', 'carnolina']
for magician in magicians:
    print(magician.title() + ', that was a great trick!')
    print('I can\'t wait to see your next trick, ' + magician.title() + '.\n')
print('Thank you, everyone. That was a great magic show!')

# for magician in magicians:
# IndentationError

# message = 'Hello Python'
#     print(message)
# IndentationError. Unnecessarily indent

numbers = [1, 2, 3]
for number in numbers:
    print(number)

    print('Loop end.') # indenting unnecessarily after the loop produce logical error.

# Practice
favorite_pizzas = ['A', 'C', 'E']
for pizza in favorite_pizzas:
    print('I like ' + pizza + ' pizza!')
print('A pizza is the most cool pizza.')
print('I really love pizza!')

animals = ['🐔', '🦆', '🐶']
for animal in animals:
    print('A ' + animal + ' would make a great pet.')
print('Any of these animals would make a great pet.')


# range function
for value in range(1, 5): # off-by-one behavior
    print(value)

numbers = list(range(1, 5))
print(numbers)

numbers = list(range(2, 11, 2))
print(numbers)

squares = []
for value in range(1, 11):
    square = value ** 2
    squares.append(square)
print(squares)

# Statistics with a list of numbers
digits = [1, 2, 3, 4, 5]
print(min(digits))
print(max(digits))
print(sum(digits))

# List Comprehension
squares = [value ** 2 for value in range(1, 11)]
print(squares)


# Practice
print('\n\n')
for number in range(1, 21):
    print(number)

girls = list(range(1, 1000001))
# for girl in girls:
#     print(girl)
print(min(girls))
print(max(girls))
print(sum(girls))

# Odd numbers
for number in range(1, 21, 2):
    print(number)

multiples = []
for value in range(3, 31):
    multiples.append(value * 3)
print(multiples)

cubes = []
for value in range(1, 11):
    cube = value ** 3
    print(cube)
    cubes.append(cube)

cubes = [value ** 3 for value in range(1, 11)]
print(cubes)

print(cubes[:3])
middle = int(len(cubes)/2)
print(cubes[middle-1:middle+1]) # get the middle two items
print(cubes[len(cubes)-3:])