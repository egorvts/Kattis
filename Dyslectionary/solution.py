from sys import stdin

dicts = []
d = []

for line in stdin:
    if line == "\n":
        for i in range(len(d)):
            d[i] = d[i][::-1]
        dicts.append(d)
        d = []
    else:
        d.append(line[:-1])
for i in range(len(d)):
    d[i] = d[i][::-1]
dicts.append(d)

for d in dicts:
    max_len = 0
    d.sort()
    for i in range(len(d)):
        d[i] = d[i][::-1]
        max_len = max(max_len, len(d[i]))

    for i in range(len(d)):
        if len(d[i]) < max_len:
            d[i] = " " * (max_len - len(d[i])) + d[i]
        print(d[i])

    if d != dicts[-1]:
        print()
