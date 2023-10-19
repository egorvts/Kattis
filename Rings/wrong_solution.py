n, m = map(int, input().split())
img = []

for i in range(n):
    img.append(list(input()))


def min_n(i, j):
    num = 50
    for i in [img[i][j-1], img[i][j+1], img[i-1][j], img[i+1][j]]:
        if i != "T" and i != ".":
            num = min(int(i), num)
    return num


count = 2
while count <= 50:
    for i in range(n):
        for j in range(m):
            if img[i][j] == "T":
                if i == 0 or j == 0 or i == n-1 or j == m-1 or img[i][j-1] == "." or img[i][j+1] == "." or img[i-1][j] == "." or img[i+1][j] == ".":
                    img[i][j] = "1"
                else:
                    img[i][j] = min_n(i, j) + 1



    count += 1


for i in img:
    print(*i)
