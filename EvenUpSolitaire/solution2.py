n = int(input())
cards = list(map(int, input().split()))

i = 0
while True:
    # print(i)
    print(cards)
    try:
        if (cards[i] + cards[i+1]) % 2 == 0:
            cards.pop(i)
            cards.pop(i+1)
        else:
            i += 1
    except IndexError:
        break

print(cards, len(cards))
