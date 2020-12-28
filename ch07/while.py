# current_number = 1
# while current_number <= 5:
#     print(current_number)
#     current_number += 1

# Letting the user choose when to quit
prompt = '\nTell me something, and I will repeat it back to you.'
prompt += '\nEnter quit or exit to end the program. '
# message = ''
# while message != 'quit' and message != 'exit':
#     message = input(prompt)
#     if message != 'quit' and message != 'exit':
#         print(message)

# Using a flag
# active = True
# while active:
#     message = input(prompt)
#     if message == 'quit' or message == 'exit':
#         active = False
#     else:
#         print(message)

# Using break to exit a loop
# while True:
#     city = input('Please input a city you have visited ' +  
#         'or you can enter \'exit\' to exit: ')
#     if city == 'exit':
#         break
#     else:
#         print('i\'d love to go to ' + city.title() + '!')

# Using continue in a loop
# current_number = 0
# while current_number < 10:
#     current_number += 1
#     if current_number % 2 == 0:
#         continue
#     print(current_number)

# Avoiding infinite loops
x = 1
while x <= 5:
    print(x)
    # x += 1
