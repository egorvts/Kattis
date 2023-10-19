from sys import stdin

counts = [0, 0, 0, 0]
len_inp = 0
inp = stdin.readline()[:-1]
for i in inp:
    len_inp += 1
    i = int(ord(i))
    if i == 95:
        counts[0] += 1
    elif 97 <= i <= 122:
        counts[1] += 1
    elif 65 <= i <= 90:
        counts[2] += 1
    else:
        counts[3] += 1

for i in counts:
    print(i/len_inp)