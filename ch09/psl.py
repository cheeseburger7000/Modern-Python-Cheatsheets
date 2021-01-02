from collections import OrderedDict
from random import randint

user_id_relationship = OrderedDict()
user_id_relationship['luca'] = 0
user_id_relationship['bruce'] = 2
user_id_relationship['jordan'] = 30

for user, id in user_id_relationship.items():
    print(user.title() + '\'s is is ' + str(id) + '.')


# returns a number between 1 and 6
x = randint(1,6)
print(x)