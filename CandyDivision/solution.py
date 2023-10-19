from math import ceil

n = int(input())
dividers = set()
for i in range(1, ceil(n**(1/2))+1):
    if n % i == 0:
        dividers.add(i-1)
        dividers.add(n//i-1)

print(" ".join(map(str, sorted(dividers))))
