names = ['luca', 'bruce', 'kobe', 'jordan']
print(names[0])
print(names[0].title())
print(names[-1])
print(names[-2])

message = 'My name is ' + names[0].title() + '.'
print(message)

# Changing, adding, and removing el
actors = ['行者', '🐷', '👴']
print(actors)
actors[0] = '🐒'
print(actors)

#actors[3] = '💩' # IndexError
actors.append('💩')
print(actors)
actors.insert(1, '唐僧')
print(actors)

del actors[4]
print(actors)

worker = actors.pop() # mutable
print(worker)
print(actors)
boss = actors.pop(1)
print(boss)
print(actors)

actors.remove('🐷')
print(actors)
#actors.remove('唐僧') # ValueError: 唐僧 not in list
print(actors)


# Practice
guest_list = ['kobe', 'james', 'jordan']
print('Inviting ' + guest_list[0] + ' to dinner.')
print('Inviting ' + guest_list[1] + ' to dinner.')
print('Inviting ' + guest_list[2] + ' to dinner.')

cannot_make = guest_list[1]
print(cannot_make + ' cannot make the dinner.')

print('\nSend out a new of invitations...\n')
guest_list[1] = 'harden'
print('Inviting ' + guest_list[0] + ' to dinner.')
print('Inviting ' + guest_list[1] + ' to dinner.')
print('Inviting ' + guest_list[2] + ' to dinner.')

print('\nFound a bigger dinner table!\n')

guest_list.insert(0, 'luca')
guest_list.insert(2, 'bruce')
# guest_list.insert(-1, 'bruce') # wrong way
guest_list.append('superman')
print('The count of People be invited: ', len(guest_list))
print('Inviting ' + guest_list[0] + ' to dinner.')
print('Inviting ' + guest_list[1] + ' to dinner.')
print('Inviting ' + guest_list[2] + ' to dinner.')
print('Inviting ' + guest_list[3] + ' to dinner.')
print('Inviting ' + guest_list[4] + ' to dinner.')
print('Inviting ' + guest_list[5] + ' to dinner.')

print('\nI can invite only two people for dinner.\n')
superman = guest_list.pop()
sorry_msg = ' sorry i cannot invite you to dinner.'
print(superman + sorry_msg)
jordan = guest_list.pop()
print(jordan + sorry_msg)
harden = guest_list.pop()
print(harden + sorry_msg)
bruce = guest_list.pop()
print(bruce + sorry_msg)

print(guest_list[0], ' you are still invited.')
print(guest_list[1], ' you are still invited.')

del guest_list[1]
del guest_list[0]
print(guest_list, '\n\n')


# Organizing a list
# sorted and sort
cars = ['bmw', 'audi', 'toyota', 'subaru']
print(sorted(cars)) # temporarily
print(cars)

cars = ['bmw', 'audi', 'toyota', 'subaru']
cars.sort() # permanently. sort alphabetically
cars.sort(reverse=True)
print(cars)

# reverse
cars = ['bmw', 'audi', 'toyota', 'subaru']
cars.reverse()
print(cars)

# len 刻薄
cars = ['bmw', 'audi', 'toyota', 'subaru']
print(len(cars))


# Practice
print('\n\n')
places_to_visit = ['hongkong', 'america', 'taipei', 'new york', 'ohio']
print(places_to_visit)

print(sorted(places_to_visit))
print(places_to_visit)

print(sorted(places_to_visit, reverse=True))
print(places_to_visit)

places_to_visit.reverse()
print(places_to_visit)

places_to_visit.sort()
print(places_to_visit)