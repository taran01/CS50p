def main():
    text = input("Input: ").strip()
    output = no_vowels(text)
    print(output)


def no_vowels(s):
    out = ""
    for c in s:
        if c.lower() not in ["a", "e", "i", "o", "u"]:
            out += c
    return out


main()