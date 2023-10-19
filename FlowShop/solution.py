n, m = map(int, input().split())
swathers = []

for line in range(n):
    swathers.append(list(map(int, input().split())))


def solution(swathers: list) -> list:

    for i in range(n):
        for j in range(m):
            if i == 0:
                if j == 0:
                    continue
                swathers[i][j] += swathers[i][j-1]
            elif j == 0:
                swathers[i][j] += swathers[i-1][j]
            else:
                swathers[i][j] += max(swathers[i-1][j], swathers[i][j-1])

    for i in range(len(swathers)):
        swathers[i] = swathers[i][-1]

    return swathers


print(*solution(swathers))

