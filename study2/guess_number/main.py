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


guess(10)