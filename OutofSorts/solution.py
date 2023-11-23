from sys import stdin

n, m, a, c, x = [int(x) for x in stdin.readline()[:-1].split()]

seq = [(a * x + c) % m]
for _ in range(n-1):
    seq.append((a * seq[-1] + c) % m)


def binary_search(a, x, left, right):
    if not right >= left:
        return False
    mid = int((right + left) / 2)
    if a[mid] == x:
        return True
    elif a[mid] > x:
        return binary_search(a, x, left, mid-1)
    else:
        return binary_search(a, x, mid+1, right)


res = 0
for i in range(n):
    if binary_search(seq, seq[i], 0, len(seq)-1):
        res += 1

print(res)
