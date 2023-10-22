import heapq as hq

n = int(input())
quests = []
energy = dict()

for i in range(n):
    inp = input()
    if inp[0] == "a":
        cmd, e, g = inp.split()
        e, g = int(e), int(g)
        hq.heappush(quests, (-e, g))
        if e in energy:
            energy[e].append(g)
        else:
            energy[e] = [g]
    else:
        cmd, x = inp.split()
        x = int(x)
        gold = 0
        print(quests)
        while quests:
            if x <= 0:
                break
            
        print(gold)
                