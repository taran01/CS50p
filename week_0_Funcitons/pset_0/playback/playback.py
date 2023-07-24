input = input()
output = ""
for c in input:
    if c.isspace():
        c = "..."
    output += c
print(output)