from sys import stdin
lst = []
first_space = True
while True:
    inp = stdin.readline()[:-1]
    if inp == "0":
        print("\n".join(lst[:-1]))
        break
    else:
        # if first_space:
        #     first_space = False
        # else:
        #     print()
        k, s = int(inp[0]), list(map(int, inp[1:].split()))
        for a in range(k-5):
            for b in range(a+1, k-4):
                for c in range(b+1, k-3):
                    for d in range(c+1, k-2):
                        for e in range(d+1, k-1):
                            for f in range(e+1, k):
                                # print(s[a], s[b], s[c], s[d], s[e], s[f])
                                lst.append(" ".join(map(str, [s[a], s[b], s[c], s[d], s[e], s[f]])))
        lst.append("")

