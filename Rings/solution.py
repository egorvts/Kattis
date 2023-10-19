n, m = map(int, input().split())
img = []


def min_n(i, j):
    num = 50
    for i in [img[i][j-1], img[i][j+1], img[i-1][j], img[i+1][j]]:
        if i != "T" and i != ".":
            num = min(int(i), num)
    return num


for i in range(n):
    img.append(list(input()))

max_ring = 0
for i in range(n):
    for j in range(m):
        if img[i][j] == "T" and (i == 0 or i == n-1 or j == 0 or j == m-1 or img[i][j-1] == "." or img[i][j+1] == "." or img[i-1][j] == "." or img[i+1][j] == "."):
            img[i][j] = "1"
            max_ring = 1

while True:
    has_t = False

    for i in range(1, n-1):
        for j in range(1, m-1):
            if img[i][j] == "T":
                if min_n(i, j) == max_ring:
                    img[i][j] = max_ring + 1
                    has_t = True

    if not has_t:
        break
    else:
        max_ring += 1

if max_ring < 10:
    cell_size = 2
else:
    cell_size = 3


def format(x):
    if cell_size == 2:
        return f".{x}"
    else:
        if len(str(x)) == 1:
            return f"..{x}"
        return f".{x}"


print("\n".join(["".join(map(format, i)) for i in img]))
