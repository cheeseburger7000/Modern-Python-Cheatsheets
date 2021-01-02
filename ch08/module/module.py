# Import an entire module
# import pizza
#
# pizza.make_pizza(16, 'pepperoni')
# pizza.make_pizza(10, 'shit', 'dog food')

# Importing specific funtions
# from pizza import make_pizza
#
# make_pizza(16, 'pepperoni')
# make_pizza(10, 'shit', 'dog food')

# Using as to give a function an alias
# from pizza import make_pizza as mp
# mp(16, 'pepperoni')
# mp(12, 'ops1', 'ops2', 'ops3')

# Using as to give a module an alias
# import pizza as p
# p.make_pizza(12, 'ops1')
# p.make_pizza(10, 'ops2', 'ops3', 'ops4')

# Importing all functions in a module
from pizza import *

make_pizza(12, 'ops1')
make_pizza(12, 'ops1', 'ops2', 'ops3')