n, k = map(int, input().split())

places = []
for _ in range(n):
    x, t = map(int, input().split())
    places.append((x, t))

places.sort(key=lambda x: x[0])

coordinates = []
letters = []
for i in range(n):
    coordinates.append(places[i][0])
    letters.append(places[i][1])

res = 0
for i in range(n-1):
    one_way = (letters[i] // k) * abs(coordinates[i])
    res += 2 * one_way
    letters[i] %= k
    if letters[i] != 0:
        res += one_way + abs(letters[i] - letters[i+1])
        letters[i+1] -= k - letters[i]
    print(letters)

print(res)


