total, found = map(int, input().split())
all_found = [0] * total

for i in range(found):
    all_found[int(input())] = 1

diff_found = 0
for i in range(total):
    if not all_found[i]:
        print(i)
    else:
        diff_found += 1

print(f"Mario got {diff_found} of the dangerous obstacles.")
