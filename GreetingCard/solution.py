import math as m

def dots_distance_2018(dot):
    x, y = dot
    return [(x - 2018, y),
            (x, y - 2018),
            (x + 2018, y),
            (x, y + 2018),
            (x + 1118, y + 1680),
            (x - 1118, y - 1680),
            (x + 1118, y - 1680), 
            (x - 1118, y + 1680),
            (x + 1680, y + 1118),
            (x - 1680, y - 1118),
            (x + 1680, y - 1118), 
            (x - 1680, y + 1118)
            ]


n = int(input())
dots = set()
for i in range(n):
    x, y = map(int, input().split())
    dots.add((x, y))

dots_list = list(dots)

pairs = 0
for d in dots_list:
    for d1 in dots_distance_2018(d):
        if d1 in dots:
            pairs += 1
    dots.remove(d)
    
print(pairs)
