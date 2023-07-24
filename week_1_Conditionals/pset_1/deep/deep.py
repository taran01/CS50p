input = input("What is the answer to the Greatest Question of Life, the Universe and Everything? ")
input = input.lower().strip()
if input in ["42", "forty-two", "forty two"]:
    print("Yes")
else:
    print("No")