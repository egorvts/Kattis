from sys import stdin
import heapq as hq

for line in stdin:
    pattern = list(map(int, list(line)[:-1]))

    # сумма – не целое число
    if sum(pattern) % len(pattern) != 0:
        print(f"{line[:-1]}: invalid # of balls")
        continue

    balls_count = sum(pattern) // len(pattern)
    beats = set()

    for i in range(len(pattern)):
        beats.add((pattern[i] + i) % len(pattern))

    if len(beats) != len(pattern):
        print(f"{line[:-1]}: invalid pattern")
    else:
        print(f"{line[:-1]}: valid with {balls_count} balls")
