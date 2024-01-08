from math import sinh, cosh
d, s = map(int, input().split())

def calc(a):
    return round(a * cosh(d / 2 * a) - a, 5)

for a in range(1, 10):
    print(calc(a))