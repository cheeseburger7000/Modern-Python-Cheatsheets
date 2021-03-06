class Car():
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0
    
    def get_descriptive_name(self):
        long_name = str(self.year) + ' ' + self.make + ' ' + self.model
        return long_name.title()

    def read_odometer(self):
        print('This car has ' + str(self.odometer_reading) + ' miles on it.')

    def update_odometer(self, mileage):
        if mileage >= self.odometer_reading:
            self.odometer_reading = mileage
        else:
            print('You can\'t roll back an odometer!')
    
    # Overriding methods from the parent class
    def fill_gas_tank(self):
        print('Oh yeah babe~')

# my_new_car = Car('audi', 'a4', 2016)
# print(my_new_car.get_descriptive_name())
# my_new_car.read_odometer()
# # Modifying an attribute's value directly
# my_new_car.odometer_reading = 23
# my_new_car.read_odometer()
# # Modifying an attribute's value through a method
# my_new_car.update_odometer(0)
# my_new_car.update_odometer(24)
# my_new_car.read_odometer()
