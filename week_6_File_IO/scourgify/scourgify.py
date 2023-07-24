import csv
from sys import exit, argv


if len(argv) < 3:
    exit("Too few command-line arguments")
if len(argv) > 3:
    exit("Too many command-line arguments")
if not argv[1].endswith(".csv"):
    exit("Not a csv file")

students = []

try:
    with open(argv[1]) as in_file:
        reader = csv.DictReader(in_file)
        for row in reader:
            students.append({"name": row["name"], "house": row["house"]})

except FileNotFoundError:
    exit("Could not read csv file")

with open(argv[2], "w") as out_file:
    writer = csv.DictWriter(out_file, fieldnames=["first", "last", "house"])
    writer.writeheader()
    for student in students:
        last, first = student["name"].split(", ")
        writer.writerow({"first": first, "last": last, "house": student["house"]})
