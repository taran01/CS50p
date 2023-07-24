import re
import sys


def main():
    print(parse(input("HTML: ")))


def parse(s):
    if matches := re.search(r"^<iframe.+(https?://(?:www\.)?youtube\.com/embed/[^\"]+)", s, re.IGNORECASE):
        return re.sub(r"https?://(www\.)?youtube\.com/embed/", "https://youtu.be/", matches.group(1))
    else:
        return None


if __name__ == "__main__":
    main()