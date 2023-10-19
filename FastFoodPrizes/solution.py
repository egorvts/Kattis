for test in range(int(input())):
    total = 0
    n, m = map(int, input().split())  # n – types of prizes, m – types of stickers
    prizes = []
    for prize in range(n):
        prizes.append(list(map(int, input().split()))[1:])
    stickers = list(map(int, input().split()))
    for i in range(n):
        total += prizes[i][-1] * min(map(lambda p: stickers[p-1], prizes[i][:-1]))
    print(total)
    '''
    prizes = {}  # prize: [stickers to get]
    for prize in range(n):
        inp = list(map(int, input().split()))
        stickers_required = inp[1:-1]
        money = inp[-1]
        prizes[money] = stickers_required
    collected = list(map(int, input().split()))
    prizes = dict(sorted(prizes.items(), reverse=True))  # prizes dict reverse
    for money, stickers in zip(prizes, prizes.values()):
        types_needed = []
        for type in stickers:
            types_needed.append(collected[type-1])
        total += min(types_needed) * money
        for ind in range(len(collected)):
            if ind in types_needed:
                collected[ind-1] = min(types_needed)

    print(total)
    '''
