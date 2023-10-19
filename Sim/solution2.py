from collections import deque
from random import choice
from string import ascii_lowercase, digits

def solution(inp1):
    for _ in range(int(input())):
        inp = [i for i in (inp1.lstrip("<[]").rstrip("[]"))]
        outp = deque()

        part = deque()
        is_start = False
        for i in range(len(inp)):
            if inp[i] in "[]":
                if is_start:
                    outp.appendleft(part)
                    part = deque()
                if inp[i] == "[":
                    is_start = True
                else:
                    is_start = False
                    outp.appendleft(part)
                    part = deque()
            elif inp[i] == "<":
                if is_start and part:
                    part.pop()
                elif outp:
                    outp[-1].pop()
            else:
                if is_start:
                    part.append(inp[i])
                else:
                    if outp:
                        outp[-1].append(inp[i])
                    else:
                        outp.append(deque(inp[i]))
        if part:
            outp.appendleft(part)

        for list in outp:
            print("".join(list), end="")
        print()

def oracle():
    chars = ascii_lowercase + digits + "<[]"
    inp = ""
    for _ in range(1_000):
        inp += choice(chars)
    solution(inp)

oracle()