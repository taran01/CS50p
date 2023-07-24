due = 50
while True:
    print(f"Amount Due: {due}")
    coin = int(input("Insert Coin: "))
    if coin in [25, 10, 5]:
        due -= coin
    if due <= 0:
        print(f"Change Owed: {abs(due)}")
        break
