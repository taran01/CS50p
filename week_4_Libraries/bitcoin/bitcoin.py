from sys import argv, exit
import requests


if len(argv) != 2:
    exit("Missing command-line argument")

try:
    buy = float(argv[1])
except ValueError:
    exit("Command-line argument is not a number")

response = requests.get("https://api.coindesk.com/v1/bpi/currentprice.json")
o = response.json()

price = o["bpi"]["USD"]["rate"]
price = float(price.replace(",", ""))
cost = buy * price

print(f"${cost:,.4f}")
