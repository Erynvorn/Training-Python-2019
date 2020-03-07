import random
guess = ''
while guess not in ('heads','tails'):
    print('Guess the coin toss! Enter heads or tails:')
    guess = input()
    if guess == 'heads':
        guess1 = 0
    elif guess == 'tails':
        guess1 = 1
toss = random.randint(0,1)
if toss == guess1:
    print('You got it')
else:
    print('Nope! Guess again!')
    guess2 = input()
    if toss == guess2:
        print('you got this')
    else:
        print('Nope')
