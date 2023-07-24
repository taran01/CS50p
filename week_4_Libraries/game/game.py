from random import randint
from sys import exit


def main():
    level = get_input("Level: ")
    if level == 0:
        print("You need to enter level!")
        exit()

    number = randint(1, level)

    while True:
        guess = get_input("Guess: ")

        if guess == 0:
            print("You give up!")
            exit()
        elif guess < number:
            print("Too small!")
        elif guess > level:
            print("Out of range")
            exit()
        elif guess > number:
            print("Too large!")
        else:
            print("Just right!")
            exit()


def get_input(s):
    while True:
        try:
            n = int(input(s))
        except EOFError:
            print()
            return 0
        except:
            pass
        else:
            if n > 0:
                return n


main()