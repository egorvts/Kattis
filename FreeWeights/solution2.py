from sys import stdin


def is_paired(r):
    size = len(r)
    if size == 0:
        return True
    elif size % 2 != 0:
        return False
    for i in range(0, size, 2):
        if r[i] != r[i+1]:
            return False
    return True


def filter_weights(r, m):
    return list(filter(lambda x: x > m, r))


n = int(input())
row1 = list(map(int, stdin.readline()[:-1].split()))
row2 = list(map(int, stdin.readline()[:-1].split()))
weights = set()
for w in row1:
    weights.add(w)
for w in row2:
    weights.add(w)
weights = sorted(weights)

if is_paired(row1) and is_paired(row2):
    print("0")
else:
    low, high = 0, len(weights)
    while low < high:
        mid = (low + high) // 2
        m = weights[mid]
        filtered_row1 = filter_weights(row1, m)
        filtered_row2 = filter_weights(row2, m)
        if is_paired(filtered_row1) and is_paired(filtered_row2):
            high = mid
        else:
            low = mid + 1
            row1 = filtered_row1
            row2 = filtered_row2

    print(weights[low])
