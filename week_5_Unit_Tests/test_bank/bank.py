def main():
    greeting = input("Greeting: ").strip()
    print(f"${value(greeting)}")


def value(greeting):
    s = greeting.lower()
    if s.startswith("hello"):
        return 0
    elif s.startswith("h"):
        return 20
    else:
        return 100


if __name__ == "__main__":
    main()