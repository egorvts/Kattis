from collections import deque

n = int(input())
cards = list(map(int, input().split()))

s1 = deque(cards)
s2 = deque()

while s1 != deque():
    if s2 != deque():
        card1 = s1.popleft()
        card2 = s2.popleft()
        if card1 % 2 != card2 % 2:
            s2.appendleft(card2)
            s2.appendleft(card1)
    else:
        card1 = s1.popleft()
        if s1 == deque():
            s2.appendleft(card1)
        else:
            card2 = s1.popleft()
            if card1 % 2 != card2 % 2:
                s2.appendleft(card1)
                s2.appendleft(card2)

print(len(s2))
