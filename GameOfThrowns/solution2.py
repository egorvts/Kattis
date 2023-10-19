from collections import deque

n, k = map(int, input().split())
commands = list(input().split())

moves = deque([0])
i = 0
while i < len(commands):
    if commands[i] == "undo":
        m = int(commands[i+1])
        for _ in range(m):
            moves.popleft()
        i += 2
    else:
        last_move = moves[0]
        m = int(commands[i])
        new = (m + last_move) % n
        moves.appendleft(new)
        i += 1

print(moves[0])
