from collections import deque
from math import ceil, floor
import sys

front = deque()
back = deque()


def balance():
    diff = len(front) - len(back)
    if diff > 1:
        for _ in range(floor(diff/2)):
            back.appendleft(front.pop())
    elif diff < 0:
        for _ in range(ceil(diff/-2)):
            front.append(back.popleft())


for _ in range(int(input())):

    op, el = sys.stdin.readline().split()

    if op == "get":
        el = int(el)
        if el >= len(front):
            el -= len(front)
            print(back[el])
        else:
            print(front[el])
    else:
        if op == "push_front":
            front.appendleft(el)
        elif op == "push_back":
            back.append(el)
        elif op == "push_middle":
            front.append(el)
        balance()

# print(front, back)
