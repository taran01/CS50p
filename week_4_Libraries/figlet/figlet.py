from pyfiglet import Figlet
from sys import argv, exit
from random import choice

figlet = Figlet()
fonts = figlet.getFonts()

if len(argv) == 1:
    text = input("Input: ")
    figlet.setFont(font=choice(fonts))
    print(figlet.renderText(text))

elif len(argv) == 3:
    f = argv[2]

    if f not in fonts:
        exit("Invalid usage")
    if argv[1] not in ["-f", "--font"]:
        exit("Invalid usage")

    text = input("Input: ")
    figlet.setFont(font=f)
    print(figlet.renderText(text))

else:
    exit("Invalid usage")
