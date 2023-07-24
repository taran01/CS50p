from sys import exit, argv
from PIL import Image, ImageOps
import os

if len(argv) != 3:
    exit("Use only two command-line argument")

if not argv[1].endswith((".jpg", ".jpeg", ".png")):
    exit("Invalid input")
if not argv[2].endswith((".jpg", ".jpeg", ".png")):
    exit("Invalid input")

in_extension = f".{argv[1].split('.')[-1]}"
out_extension = os.path.splitext(argv[2])[-1]
if in_extension != out_extension:
    exit("Input and output have different extensions")

try:
    shirt = Image.open("shirt.png")
    input = Image.open(argv[1])
except FileNotFoundError:
    exit("File not found")

size = shirt.size
resized = ImageOps.fit(input, size, bleed=0.0, centering=(0.5, 0.5))
resized.paste(shirt, shirt)
resized.save(argv[2])
