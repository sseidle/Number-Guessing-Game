import random


def guess(x):
    random_number = random.randint(1, x)
    approximate = 0
    while approximate != random_number:
        approximate = int(input(f'guess a number between 1 and {x}: '))
        if approximate < random_number:
            print('Sorry, guess again. Too low.')
        elif approximate > random_number:
            print('Sorry, guess again. Too high.')
        if approximate == random_number:
            print(f'yay, congrats. You have guessed the number {random_number} correctly!!')


guess(10)
