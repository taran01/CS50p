import re
import inflect
from sys import exit
from datetime import date


p = inflect.engine()


def main():
    dob = get_dob(input("Date of Birth: "))
    minutes = difference(dob)

    words = p.number_to_words(minutes, andword="").capitalize()
    print(words, "minutes")


def get_dob(s):
    if match := re.search(r"^(\d{4}-\d{2}-\d{2})$", s):
        year, month, day = match.group(1).split("-")
        try:
            return date(int(year), int(month), int(day))
        except (OverflowError, ValueError):
            exit("Invalid date")
    else:
        exit("Invalid date")


def difference(dob):
    today = date.today()
    difference_days = today - dob
    minutes = str(difference_days * 24 * 60).split(" ", 1)[0]
    return minutes


if __name__ == "__main__":
    main()
