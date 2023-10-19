r, n = map(int, input().split())
if n == r:
    print("too late")
else:
    rooms = [0] * r
    for i in range(n):
        taken = int(input())
        rooms[taken-1] = 1
    for room in range(r):
        if rooms[room] == 0:
            print(room+1)
            break