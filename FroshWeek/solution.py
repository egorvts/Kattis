from collections import deque

n, m = map(int, input().split())
tasks = list(map(int, input().split()))
quiet = list(map(int, input().split()))

tasks.sort(reverse=True)
quiet.sort(reverse=True)

tasks = deque(tasks)
quiet = deque(quiet)

res = 0
while tasks and quiet:
    if quiet[0] >= tasks[0]:
        res += 1
        tasks.popleft()
        quiet.popleft()
    else:
        tasks.popleft()
    
print(res)
