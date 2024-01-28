for t in range(int(input())):
    n = int(input())
    v1 = list(map(int, input().split()))
    v2 = list(map(int, input().split()))

    v1.sort()
    v2.sort(reverse=True)

    prod = 0
    for i in range(n):
        prod += v1[i] * v2[i]

    print(f"Case #{t+1}: {prod}")
