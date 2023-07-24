from sys import argv, exit


if len(argv) != 2:
    exit("Usage: python lines.py filename")

if not argv[1].endswith(".py"):
    exit("Not a Python file")

lines = 0

try:
    with open(argv[1]) as file:
        for line in file:
            if line.strip().startswith("#"):
                continue
            elif line.strip() == "":
                continue
            else:
                lines += 1

except FileNotFoundError:
    exit("File does not exist")

print(lines)