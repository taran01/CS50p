def main():
    text = input("Input: ").strip()
    output = shorten(text)
    print(output)


def shorten(word):
    out = ""
    for c in word:
        if c.lower() not in ["a", "e", "i", "o", "u"]:
            out += c
    return out


if __name__ == "__main__":
    main()