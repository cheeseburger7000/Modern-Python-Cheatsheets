# Passing a list
# def to_string_datasource(datasources):
#     for datasource in datasources:
#         result = 'Datasource name: ' + datasource.title() + '.'
#         print(result)

# datasources = ['ds1', 'ds2', 'ds3']
# to_string_datasource(datasources)

# Modifying a list in a function
# def print_models(unprinted_designs, completed_models):
#     while unprinted_designs:
#         current_design = unprinted_designs.pop()
#         print('Printing model: ' + current_design)
#         completed_models.append(current_design)

# def show_completed_models(completed_models):
#     print('\nResult: ')
#     for completed_model in completed_models:
#         print(completed_model)

# unprinted_designs = ['a1', 'a2', 'a3']
# completed_models = []

# # print_models(unprinted_designs[:], completed_models) # Preventing a function from modifying a list
# print_models(unprinted_designs, completed_models)
# show_completed_models(completed_models)

# Passing an arbitrary number of arguments
# def make_pizza(*toppings): # tuple
#     for topping in toppings:
#         print('- ' + topping)

# make_pizza('pepperoni')
# make_pizza('mushrooms', 'green peppers', 'extra cheese')

# Mixing positional anf arbitrary arguments
# def make_pizza(size, *toppings):
#     print('Making a ' + str(size) + '-inch pizza with the following toppings:')
#     for topping in toppings:
#         print('- ' + topping)

# make_pizza(16, 'pepperoni')
# make_pizza(12, 'mushrooms', 'green peppers', 'extra cheese')

# Using arbitrary keyword arguments
def build_profile(first, last, **user_info):
    profile = {}
    profile['first_name'] = first
    profile['last_name'] = last
    for key, value in user_info.items():
        profile[key] = value
    return profile

user_profile = build_profile('shaohsiung', 'yeung', location='america', field='python')
print(user_profile)