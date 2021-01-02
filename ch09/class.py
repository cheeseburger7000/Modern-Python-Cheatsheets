# Greating the dog class
class Dog():
    '''
    A simple attempt to model a dog.
    this is a docstring describing what this class does. 
    class instance method attribute
    '''
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def sit(self):
        print(self.name.title() + ' is now sitting.')

    def roll_over(self):
        print(self.name.title() + ' rolled over!')

# Accessing attributes
my_dog = Dog('willie', 6)
print(my_dog.name.title())
print(my_dog.age)

# Calling methods
my_dog.sit()
my_dog.roll_over()

# Creating multiple instances
your_dog = Dog('luca', 3)
your_dog.sit()
your_dog.roll_over()
