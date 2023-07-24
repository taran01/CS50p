def main():
    fraction = input("Fracton: ")
    converted = convert(fraction)
    fuel = gauge(converted)
    print(fuel)


def convert(fraction):
    while True:
        s = fraction
        try:
            x, y = s.split(sep="/")
            if int(x) > int(y):
                raise ValueError
            return round(int(x) / int(y) * 100)
        except (ValueError, ZeroDivisionError):
            pass


def gauge(percentage):
    if percentage <= 1:
        return "E"
    elif percentage >= 99:
        return "F"
    else:
        return f"{percentage}%"



if __name__ == "__main__":
    main()