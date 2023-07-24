import inflect

p = inflect.engine()

names = list()
while True:
    try:
        name = input("Name: ")
        names.append(name)
    except EOFError:
        print()
        break

mylist = p.join(names)
print(f"Adieu, adieu, to {mylist}")