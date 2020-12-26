players = ['kobe', 'james', 'michael', 'luca', 'allen']
print(players[1:3])
print(players[:3]) # ['kobe', 'james', 'michael']
print(players[2:]) # ['michael', 'luca', 'allen']
print(players[-3:]) # ['michael', 'luca', 'allen']

print('The first three players on my team: ')
for player in players[:3]:
    print(player.title())