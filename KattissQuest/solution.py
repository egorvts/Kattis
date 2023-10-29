import heapq as hq

n = int(input())
quests = []
q2 = []
energy = dict()

for i in range(n):
    inp = input()
    if inp[0] == "a":
        cmd, e, g = inp.split()
        e, g = int(e), int(g)
        hq.heappush(quests, (-e, g))
        if e not in energy:
            energy[e] = []
        hq.heappush(energy[e], -g)
    else:
        cmd, x = inp.split()
        x = int(x)
        gold = 0
        while quests:
            h_pop = hq.heappop(quests)
            e, g = h_pop
            e = -e
            if energy[e] and e <= x:
                gld = hq.heappop(energy[e])
                gold += -1 * gld
                x -= e
            else:
                hq.heappush(q2, h_pop)
        print(gold)
        quests = q2[:]
        q2 = []
