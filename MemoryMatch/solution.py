cards_amount = int(input())
cards = ["?"] * cards_amount

turns_played = int(input())
for t in range(turns_played):
    inp = list(input().split())
    if inp[2] == inp[3]:
        cards[int(inp[0])-1] = "face-up"
        cards[int(inp[1])-1] = "face-up"
    else:
        cards[int(inp[0])-1] = inp[2]
        cards[int(inp[1])-1] = inp[3]

output = 0
for i in range(cards_amount):
    for j in range(cards_amount):
        if i != j and cards[i] != "face-up" and cards[j] != "face-up" and cards[i] == cards[j]:
            output += 1
            cards[i] = "face-up"
            cards[j] = "face-up"

matched = 0
for c in cards:
    if c != "?" and c != "face-up":
        matched += 1

if cards.count("?") == matched:
    output += matched
elif matched == 0 and cards.count("?") == 2:
    output += 1

print(output)