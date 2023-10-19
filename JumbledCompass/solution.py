current = int(input())
correct = int(input())

diff = abs(current - correct)

step = min(diff, abs(360 - diff))

if (current + step) == correct or (current + step - 360) == correct:
    print(step)
else:
    print(-step)
