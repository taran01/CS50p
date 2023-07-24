def main():
    fraction = get_f()
    if fraction <= 1:
        print("E")
    elif fraction >= 99:
        print("F")
    else:
        print(f"{fraction}%")


def get_f():
    while True:
        s = input("Fraction: ")
        try:
            x, y = s.split(sep="/")
            if int(x) > int(y):
                raise ValueError
            return round(int(x) / int(y) * 100)
        except (ValueError, ZeroDivisionError):
            pass


main()