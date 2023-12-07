f = open("09.csv")
nums = [[int(y) for y in x.rstrip().split(",")] for x in f.readlines()]
f.close()

def check(lst):
    x, y, z = lst
    g1 = x * y
    g2 = x * z
    g3 = y * z

    return (g1 > g2 + g3) or (g2 > g1 + g3) or (g3 > g1 + g2)

print(len(list(filter(check, nums))))