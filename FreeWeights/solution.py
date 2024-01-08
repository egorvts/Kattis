from sys import stdin

n = int(input())
row1 = list(map(int, stdin.readline()[:-1].split()))
row2 = list(map(int, stdin.readline()[:-1].split()))
weights = [0] + sorted(list(set(row1 + row2)))


def is_sorted(r1, r2):
    len_r1 = len(r1)
    len_r2 = len(r2)
    if not (len_r2 % 2 == len_r2 % 2 == 0):
        return False
    for i in range(0, len_r1, 2):
        if not r1[i] == r1[i+1]:
            return False
    for i in range(0, len_r2, 2):
        if not r2[i] == r2[i+1]:
            return False
    return True


for w in weights:
    row1 = list(filter(lambda x: x > w, row1))
    row2 = list(filter(lambda x: x > w, row2))
    if is_sorted(row1, row2):
        print(w)
        break
