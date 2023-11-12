from itertools import combinations

prohibitions = []
n, m = map(int, input().split())
for i in range(m):
    a, b = map(int, input().split())
    prohibitions.append((a, b))

combos = set()

def is_valid(p):
    for i in prohibitions:
        if (i[0] in p) and (i[1] in p):
            return False
    return True

for i in range(n):
    for p in combinations(range(1, n+1), i):
        p = list(p)
        if prohibitions:
            if is_valid(p):
                combos.add("".join(map(str, p)))

if combos:
    print(len(combos))
    print(combos)
else:
    print(2 ** n)
