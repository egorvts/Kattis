from collections import deque
from string import ascii_uppercase
LETTERS = ascii_uppercase

n = int(input())
values = list(input().split())
circuit = list(input().split())
d = {}
for i in range(n):
    d[LETTERS[i]] = True if values[i] == "T" else False

res = deque([])
for i in range(len(circuit)):
    if circuit[i] == "-":
        res.appendleft(not(res.popleft()))
    elif circuit[i] == "+":
        el1 = res.popleft()
        el2 = res.popleft()
        res.appendleft(el1 or el2)
    elif circuit[i] == "*":
        el1 = res.popleft()
        el2 = res.popleft()
        res.appendleft(el1 and el2)
    else:
        res.appendleft(d[circuit[i]])

print("T" if res[0] else "F")