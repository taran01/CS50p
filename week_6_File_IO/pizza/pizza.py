import csv

from sys import exit, argv
from tabulate import tabulate


if len(argv) < 2:
    exit("Too few command-line arguments")

if len(argv) > 2:
    exit("Too many command-line arguments")

if not argv[1].endswith(".csv"):
    exit("Not a .csv file")

table = []

try:
    with open(argv[1]) as file:
        reader = csv.reader(file)
        fieldnames = next(reader)
        for line in reader:
            table.append(line)
except FileNotFoundError:
    exit("File not found")

print(table)

print(tabulate(table, headers=fieldnames, tablefmt="grid"))