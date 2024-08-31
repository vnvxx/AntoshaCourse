import random


def guess(x):
    random_nuber = random.randint(1, x)
    guess = 0
    while guess != random_nuber:
        guess = int(input(f'Guess a number between 1 and {x}: '))
        if guess < random_nuber:
            print('Sorry, so low')
        elif guess > random_nuber:
            print('Sorry, to high')

    print(f'Respect, you are a monster!!!')


def computer_guess(x):
    low = 1
    high = x
    feedback = ''
    while feedback != 'c':
        # if low != high:
        guess = random.randint(low, high)
        # else:
        #     guess = low
        feedback = input(f'Is {guess} too high (H), too low (L), or correct (C)??').lower()
        if feedback == 'h':
            high = guess - 1
        if feedback == 'l':
            low = guess + 1

    print(f'Respect to you choice comp, {guess}!!!')


computer_guess(10)