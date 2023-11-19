from math import sqrt, ceil

for t in range(int(input())):
    n, e = map(int, input().split())

    for i in range(2, ceil(sqrt(n))):
        if n % i == 0:
            p, q = i, n // i

            def y(p, q):
                return (p-1) * (q-1)

            # d = (1 % y(p, q)) // e
            for d in range(2, y(p, q)):
                k = (d * e - 1) / y(p, q)
                if k % 1 == 0:
                    print(d)
