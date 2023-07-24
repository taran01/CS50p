import re
import sys


def main():
    print(validate(input("IPv4 Address: ")))


def validate(ip):
    if matches := re.search(r"^(\d+)\.(\d+)\.(\d+)\.(\d+)$", ip):
        for digit in matches.groups():
            if int(digit) > 255:
                return False
        return True
    else:
        return False


if __name__ == "__main__":
    main()