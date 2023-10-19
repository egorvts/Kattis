from collections import deque

n, k = map(int, input().split())
commands = list(input().split())

while "undo" in commands:
    undo_ind = commands.index("undo")
    commands[undo_ind] = "undo " + commands[undo_ind+1]
    commands.pop(undo_ind+1)

moves = deque([0])
for m in commands:
    if m[0] == "u":
        c, m = m.split()
        for _ in range(int(m)):
            moves.popleft()
    else:
        last_move = moves[0]
        new = int(m) + last_move
        while not (0 <= new <= n):
            if new < 0:
                new += n
            else:
                new -= n
        moves.appendleft(new)

print(moves)
print(moves[0])
