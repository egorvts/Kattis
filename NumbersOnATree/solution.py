from sys import stdin, exit

inp = list(stdin.readline()[:-1].split())

if len(inp) == 1:
    height, path = int(inp[0]), ""
else:
    height, path = int(inp[0]), inp[1]

res = 2 ** (height + 1)
minus = 1
for i in range(len(path)):
    minus *= 2
    if path[i] == "R":
        minus += 1

print(res - minus)
