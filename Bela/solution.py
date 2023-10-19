n, b = input().split()

values_d = {"A": 11, "K": 4, "Q": 3, "J": 20, "T": 10, "9": 14, "8": 0, "7": 0}
values_n = {"A": 11, "K": 4, "Q": 3, "J": 2, "T": 10, "9": 0, "8": 0, "7": 0}

value = 0

for card in range(4*int(n)):
    card = input()
    if card[1] == b:
        value += values_d[card[0]]
    else:
        value += values_n[card[0]]

print(value)
