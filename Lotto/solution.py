from sys import stdin

first_space = True
while True:
    inp = stdin.readline()[:-1]
    if inp == "0":
        break
    else:
        if first_space:
            first_space = False
        else:
            print()
        k, s = int(inp[0]), list(map(int, inp[1:].split()))
        for a in s:
            for b in s:
                for c in s:
                    for d in s:
                        for e in s:
                            for f in s:
                                if a < b < c < d < e < f:
                                    print(a, b, c, d, e, f)
