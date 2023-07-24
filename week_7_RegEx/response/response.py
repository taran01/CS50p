from validator_collection import validators


try:
    email = input("What's your email address? ")
    if validators.email(email):
        print("Valid")
except ValueError:
    print("Invalid")