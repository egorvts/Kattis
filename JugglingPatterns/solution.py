from sys import stdin
import heapq as hq

for line in stdin:
    pattern = list(map(int, list(line)[:-1]))

    # сумма – не целое число
    if sum(pattern) % len(pattern) != 0:
        print(f"{line[:-1]}: invalid # of balls")
        continue

    balls_count = sum(pattern)//len(pattern)
    balls_left = balls_count
    h = []  # очередь
    beats = set()

    i = 0
    beat = 0

    while True:
        if i != 0 and len(beats) != 
            print(f"{line[:-1]}: invalid pattern")
            break

        # print(pattern)
        # print(i, pattern[i])
        # hq.heappush(h, (beat+1, pattern[i]))
        beats.add((beat + pattern[i]) % len(pattern))

        beat += 1
        if i == len(pattern) - 1:
            i = 0
        else:
            i += 1

        if beat > 100:
            print(f"{line[:-1]}: valid with {balls_count} balls")
            break

    # print(h, balls_count)
