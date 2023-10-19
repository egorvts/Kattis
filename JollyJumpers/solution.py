from sys import stdin

tests = []

for line in stdin:
    tests.append(list(map(int, line.split())))

for test in tests:
    diffs = list(range(1, len(test)-1))
    for i, j in zip(test[:-1], test[1:]):
        d = abs(i-j)
        if d in diffs:
            diffs.remove(d)
    if not diffs:
        print("Jolly")
    else:
        print("Not jolly")