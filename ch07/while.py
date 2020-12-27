# current_number = 1
# while current_number <= 5:
#     print(current_number)
#     current_number += 1

# Letting the user choose when to quit
prompt = '\nTell me something, and I will repeat it back to you.'
prompt += '\nEnter quit or exit to end the program. '
message = ''
while message != 'quit' and message != 'exit':
    message = input(prompt)
    if message != 'quit' and message != 'exit':
        print(message)

# Using a flag
