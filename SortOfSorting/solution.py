from functools import cmp_to_key

def sort(n1, n2):
    if n1[0] > n2[0]:
        return 1
    elif n1[0] < n2[0]:
        return -1
    else:
        if n1[1] > n2[1]:
            return 1
        elif n1[1] < n2[1]:
            return -1
    return 0

not_first = False
while True:
    n = int(input())
    if n == 0:
        break
    elif not_first:
        print()

    not_first = True
    names = []
    for _ in range(n):
        names.append(input())

    names.sort(key=cmp_to_key(sort))
    for name in names:
        print(name)