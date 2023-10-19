hand = input().split()[:5]

hand_ranks = []
counts = []

for i in hand:
    hand_ranks.append(i[0])

for i in hand_ranks:
    counts.append(hand_ranks.count(i))

print(max(counts))
