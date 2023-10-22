import heapq as hq

def heapq_remove(heap, index):
    """Remove item from heap"""

    # Move slot to be removed to top of heap
    while index > 0:
        up = (index + 1) / 2 - 1
        heap[index] = heap[up]
        index = up

    # Remove top of heap and restore heap property
    hq.heappop(heap)

commands = int(input())
cats = dict()
lvls = []
for c in range(commands):
    inp = input()
    if inp[0] == "0":
        cmd, cat, lvl = inp.split()
        cats[cat] = int(lvl)
        hq.heappush(lvls, (-int(lvl), cat))
    elif inp[0] == "1":
        cmd, cat, lvl = inp.split()
        lvls.remove((-cats[cat], cat))
        cats[cat] += int(lvl)
        hq.heappush(lvls, (-cats[cat], cat))
    elif inp[0] == "2":
        cmd, cat = inp.split()
        # print(lvls)
        # print((cats[cat], cat))
        lvls.remove((-cats[cat], cat))
        cats.pop(cat)
    else:
        if not lvls:
            print("The clinic is empty")
        else:
            max_lvl = hq.heappop(lvls)
            print(max_lvl[1])
            hq.heappush(lvls, max_lvl)
