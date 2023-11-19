def calc_max(a, b, c):
    x0 = -b / (2 * a)
    return a * x0 ** 2 + b * x0 + c

for t in range(int(input())):
    n = int(input())
    maxs = []
    for i in range(n):
        a, b, c = map(int, input().split())
        a = -a
        maxs.append((i+1, calc_max(a, b, c)))

    print(max(maxs, key=lambda x: x[1])[0])
    