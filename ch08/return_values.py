# Return a simple value
# def get_formatted_name(first_name, last_name):
#     full_name = first_name + ' ' + last_name
#     return full_name.title()

# musician = get_formatted_name('Shaohsiung', ' Yeung')
# print(musician)

# Making an argument optional
# def get_formatted_name(first_name, last_name, middle_name = ''):
#     if middle_name:
#         full_name = first_name + ' ' + middle_name + ' ' + last_name
#     else:
#         full_name = first_name + ' ' + last_name
#     return full_name.title()

# musician = get_formatted_name('Donal', 'Trump', 'J')
# print(musician)

# Returing a Dictionary
# def build_person(first_name, last_name, age = 0):
#     person = { 'first': first_name, 'last': last_name }
#     if age:
#         person['age'] = age
#     return person

# musician = build_person('yeung', 'shaohsiung')
# # musician = build_person('yeung', 'shaohsiung', 12)
# print(musician)