import re
import sys


def main():
    print(convert(input("Hours: ")))


def convert(s):
    if matches := re.search(r"(\d+(?::\d{2})?) (AM|PM) to (\d+(?::\d{2})?) (AM|PM)", s, re.IGNORECASE):
        time1,tt1,time2,tt2 = matches.groups()
        return f"{twentyFour(time1, tt1)} to {twentyFour(time2, tt2)}"
    else:
        raise ValueError


def twentyFour(time, tt):
    if len(time) > 2:
            hours, minutes = time.split(":")
            if int(hours) > 12 or int(minutes) > 59:
                raise ValueError
            else:
                if tt == "AM":
                    return f"{int(hours) % 12:02}:{int(minutes):02}"
                elif tt == "PM":
                    if int(hours) == 12:
                        return f"{int(hours):02}:{int(minutes):02}"
                    else:
                        return f"{(12 + int(hours) % 24):02}:{int(minutes):02}"
    else:
        if int(time) > 12:
            raise ValueError
        if tt == "AM":
            return f"{int(time) % 12:02}:00"
        elif tt == "PM":
            if int(time) == 12:
                return f"{int(time):02}:00"
            else:
                return f"{(12 + int(time) % 24):02}:00"


if __name__ == "__main__":
    main()