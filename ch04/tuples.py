# An immutable list is called a tuple
dimensions = (200, 50)
print(dimensions[0:2])
print(dimensions[1])

# dimensions[0] = 100 # TypeError

for dimension in dimensions:
    print(dimension)

# redefine the entire tuple
dimensions = (400, 100)
for dimension in dimensions:
    print(dimension)


# Practice
buffet_foods = ('C', 'E', 'D', 'A', 'L')
for buffet_food in buffet_foods:
    print(buffet_food)

#buffet_foods[1] = 'EE'
buffet_foods = ('C', 'EE', 'DD', 'A', 'L')
for buffet_food in buffet_foods:
    print(buffet_food)