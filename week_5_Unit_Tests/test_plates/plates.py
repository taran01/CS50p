def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):
    # Check for min-max length
    if 2 > len(s) or len(s) > 6:
        return False

    # Starts with atleast 2 letters
    if not s[0:2].isalpha():
        return False

    # Make sure s dont have any period, spaces, punctuation
    if not s.isalnum():
        return False

    # Numbers cant be in middle, first number cant be 0
    first_num = ""

    for i in range(len(s)):
        if s[i].isdigit():
            if not s[i:len(s)].isdigit():
                return False
            first_num = s[i]
            break

    if first_num == "0":
        return False

    return True



if __name__ == "__main__":
    main()