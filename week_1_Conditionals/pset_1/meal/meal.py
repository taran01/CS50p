def main():
    time = input("What time is it? ")

    converted = convert(time)

    if 7 <= converted <= 8:
        print("breakfast time")
    elif 12 <= converted <= 13:
        print("lunch time")
    elif 18 <= converted <= 19:
        print("dinner time")
    else:
        return


def convert(time):
    if len(time) <= 5:
        hours, minutes = time.split(":")
        return float(hours) + float(minutes) / 60
    else:
        hours, minutes = time.split(":")
        minutes, tt = minutes.split(" ")
        if tt in ["a.m.", "am", "a.m"]:
            return float(hours) + float(minutes) / 60
        elif tt in ["p.m.", "pm", "p.m"]:
            r = ( 12.0 + (float(hours) + float(minutes) / 60)) % 24
            if r < 1:
                return r + 12
            return r


if __name__ == "__main__":
    main()