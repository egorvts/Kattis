from collections import deque

n = int(input())
socks = deque(list(map(int, input().split())))
auxiliary_pile = deque()

moves = 0
while socks != deque():
    if auxiliary_pile != deque():
        sock1 = socks.popleft()
        sock2 = auxiliary_pile.popleft()
        if sock1 != sock2:
            moves += 1
            auxiliary_pile.appendleft(sock2)
            auxiliary_pile.appendleft(sock1)
        else:
            moves += 1

    else:
        moves += 1
        auxiliary_pile.appendleft(socks.popleft())

if socks == auxiliary_pile == deque():
    print(moves)
else:
    print("impossible")
