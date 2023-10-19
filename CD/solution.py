from sys import stdin

while True:
    n, m = map(int, input().split())
    if n == m == 0:
        break

    cds1 = set()
    for i in range(n):
        cd = int(stdin.readline()[:-1])
        cds1.add(cd)
    cds2 = set()
    for i in range(m):
        cds2.add(int(input()))
    
    print(len(cds1.intersection(cds2)))