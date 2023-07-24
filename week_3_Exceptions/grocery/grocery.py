items = {}

while True:
    try:
        item = input("")
        if item not in items:
            items[item] = 1
        else:
            items[item] += 1
    except EOFError:
        print()
        break

sorted_items = dict(sorted(items.items()))

for i in sorted_items:
    print(sorted_items[i], i.upper())