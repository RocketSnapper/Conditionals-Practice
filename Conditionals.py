import random
legal_driving_age = 16
user_age = int(input('Whats your age?'))
if user_age >= legal_driving_age:
    print('You are legally able to drive')
else:
    print('You are not old enough to drive yet')

random_number = random.randrange(0,11)
if random_number == 0 or random_number == 1 or random_number == 2:
    print('0 or 1 or 2')
elif random_number == 3 or random_number == 4 or random_number == 5:
    print('3 or 4 or 5')
elif random_number == 6 or random_number == 7 or random_number == 8:
    print('6 or 7 or 8')
else:
    print('9 or 10')

favorite_team = input('Whats your favorite NHL team?')
if favorite_team == 'Flyers':
    print('Backcheck much?')
elif favorite_team == 'Sabres':
    print('Nice powerplay!')
elif favorite_team == 'Oilers':
    print('Go Mcjesus!')
elif favorite_team == 'Predators':
    print('Go Preds!')
else:
    print('Pick a different team!')
