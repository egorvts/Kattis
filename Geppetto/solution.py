from itertools import combinations

n, m = map(int, input().split())
restrictions = set()

for i in range(m):
    a, b = map(int, input().split())
    restrictions.add((a, b))

def is_valid(p):
    for r in restrictions:
        if (r[0] in p) and (r[1] in p):
            return False
    return True

combos = set()

for i in range(n+1):
    for p in combinations(range(1, n+1), i):
        if is_valid(p):
            combos.add(p)

print(len(combos))
