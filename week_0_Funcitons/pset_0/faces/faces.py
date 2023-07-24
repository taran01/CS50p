def main():
    text = input("Input: ")
    output = convert(text)
    print(output)


def convert(s):
    c = s
    if s.find(":)"):
        c = s.replace(":)", "🙂")
    if s.find(":("):
        c = c.replace(":(", "🙁")
    return c

main()