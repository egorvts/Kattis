x, y = map(int, input().split())
shields = []
n = int(input())
for i in range(n):
    l, u, f = input().split()
    shields.append((int(l), int(u), float(f)))
shields.append((y,))  # верхняя граница (Firefly)

s = shields[0][0]
for i in range(n):
    # прибавляется (высота shield'а) * (f)
    s += (shields[i][1]-shields[i][0])*shields[i][2]

    # прибавляется высота пустой части над shield'ом
    s += shields[i+1][0]-shields[i][1]

print('%.6f' % (x / s))
