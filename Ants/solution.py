for t in range(int(input())):
    l, n = map(int, input().split())
    ants = []
    while n != 0:
        inp = list(map(int, input().split()))
        n -= len(inp)
        ants += inp

    min_time = min(ants[0], l-ants[0])
    max_time = max(ants[0], l-ants[0])
    for ant in ants:
        min_time = max(min_time, min(ant, l-ant))
        max_time = max(max_time, max(ant, l-ant))

    # ants.sort()
    # max_time = 0
    # for i in range(len(ants)-1):
    #     # print(ants[i], ants[i+1])
    #     # print((ants[i+1] - ants[i]))
    #     # print("max", max(l - ants[i+1], ants[i]))
    #     if ants[i+1] - ants[i] > 1:
    #         max_time = ((ants[i+1] - ants[i])) + max(l - ants[i+1], ants[i])

    print(min_time, max_time)
