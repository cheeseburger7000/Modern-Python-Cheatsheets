cars = ['audi', 'bmw', 'subaru', 'toyota']
for car in cars:
    if car == 'bmw':
        print(car.upper())
    else:
        print(car.title())

# Conditional tests
requested_topping = 'mashrooms'
if requested_topping != 'shit':
    print('Holy the shit')

age = 14
if age == 1:
    print('1')
elif age >= 2 and age <=10:
    print('2~10')
elif (age > 10) or (age == 12):
    print('>10 or 12')
else:
    print('other')

# value is in a list
result = 'audi' in cars
print(result)
result = 'wtf' in cars
print(result)
# value is not in a list
brand = 'ops'
if brand not in cars:
    print(brand.title() + " not found.")

game_active = True
if game_active:
    print('Staring play the f**king game!')

# Practce
# todo