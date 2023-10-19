cards_count = int(input())
turns_played = int(input())

cards = ["?"] * cards_count

for turn in range(turns_played):
    inp = input().split()
    if inp[2] != inp[3]:
        cards[int(inp[0])-1], cards[int(inp[1])-1] = inp[2], inp[3]
    else:
        cards[int(inp[0])-1] = cards[int(inp[1])-1] = "face-up"

print(cards)

output = 0
unmatched = 0
unknown = 0

for card in cards:
    if cards.count(card) == 2 and card != "face-up" and card != "?":
        cards[cards.index(card)] = "face-up"
        cards[cards.index(card)] = "face-up"
        output += 1
    elif card != "face-up" and card != "?":
        unmatched += 1
    elif card == "?":
        unknown += 1
    
print(cards, output, unmatched, unknown)

if unknown == unmatched:
    output += unknown
elif unknown == 2 and unmatched == 0:
    output += 1

print(output)