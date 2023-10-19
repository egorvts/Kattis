inp = []
complete = set()
totalTime = 0

while True:
    try:
        time, task, result = input().split()
        inp.append([int(time), task, result])
    except ValueError:
        break

for i in inp:
    if i[2] == "right":
        complete.add(i[1])

for i in inp:
    if i[2] == "right":
        totalTime += i[0]
    elif i[1] in complete and i[2] == "wrong":
        totalTime += 20

print(len(complete), totalTime)
