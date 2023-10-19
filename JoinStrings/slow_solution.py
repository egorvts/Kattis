n = int(input())
strings = []
inds = [[]] * n
last_ind = 0

for _ in range(n):
    strings.append(input())

last_ind = 0
for _ in range(n-1):
    i1, i2 = map(lambda x: int(x)-1, input().split())
    last_ind = i1
    inds[i1].append(i2)
    inds[i2] = inds[i2][1:]

print(inds)


def print_s(ind):
    print(ind)
    if inds[ind] != []:
        print(strings[ind], end="")
        for _ in range(len(inds[ind])):
            print_s(inds[ind][0])
            inds[ind].pop()
        inds[ind] = []


print_s(last_ind)
