from car import Car

class ElectricCar(Car):
    def __init__(self, make, model, year):
        super().__init__(make, model, year)
        self.battery_size = 70

    def describe_battery(self):
        print('This car has a ' + str(self.battery_size) + '-KWh battery.')

    # Override
    def fill_gas_tank(self):
        print('This car doesn\'t need a gas tank!')

my_tesla = ElectricCar('tesla', 'model s', 2016)
print(my_tesla.get_descriptive_name())
my_tesla.describe_battery()
my_tesla.fill_gas_tank()