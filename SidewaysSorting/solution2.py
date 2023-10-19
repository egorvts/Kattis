t = 0
while True:
    r, c = map(int, input().split())

    def rotate(l):
        return ["".join([l[j][i] for j in range(r)]) for i in range(c)]
    
    def rotate_back(l):
        return ["".join([l[j][i] for j in range(c)]) for i in range(r)]

    if r == c == 0:
        break
    elif t != 0:
        print()
    else:
        t += 1

    lines = []
    for _ in range(r):
        lines.append(list(input()))

    print("\n".join(rotate_back(sorted(rotate(lines), key=str.lower))))
