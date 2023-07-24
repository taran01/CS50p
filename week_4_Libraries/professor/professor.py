from random import randint


def main():
    level = get_level()
    score = 0

    for _ in range(10):
        x = generate_integer(level)
        y = generate_integer(level)
        z = x + y
        mistakes = 0

        while True:
            if mistakes == 3:
                print(f"{x} + {y} = {z}")
                break

            answer = input(f"{x} + {y} = ")

            if answer != str(z):
                print("EEE")
                mistakes += 1
            else:
                score += 1
                break

    print("Score:", score)


def get_level():
    while True:
        try:
            n = int(input("Level: "))
        except ValueError:
            pass
        else:
            if n in [1, 2, 3]:
                return n


def generate_integer(level):
    if level == 1:
        return randint(0, 9)
    elif level == 2:
        return randint(10, 99)
    else:
        return randint(100, 999)


if __name__ == "__main__":
    main()