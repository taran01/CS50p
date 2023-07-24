def main():
    text = input("camelCase: ").strip()
    output = snake_case(text)
    print(output)


def snake_case(s):
    out = ""
    for c in s:
        if c.isupper():
            out += "_"
            out += c.lower()
        else:
            out += c
    return out


main()