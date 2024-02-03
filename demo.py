import random


def guess_num(x):
    random_num = random.randint(1, x)
    guess = 0
    while guess != random_num:
        guess = int(input(f'Input any number between 1 and {x}: '))
        if guess > random_num:
            print("Too high, try again!!")
        elif guess < random_num:
            print("Too low, try again!!")

    print(f"Congratulations!! The answer is {random_num}")



a = int(input('输入一个整数开始游戏：'))
guess_num(a)