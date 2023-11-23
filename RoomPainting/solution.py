from bisect import bisect_left

n, m = map(int, input().split())

can_sizes = []

for _ in range(n):
    can_sizes.append(int(input()))

can_sizes.sort()


def find_can_size(needed):
    i = bisect_left(can_sizes, needed)
    if i != m:
        return can_sizes[i]
    return can_sizes[-1]


left = 0
for _ in range(m):
    joe_needs = int(input())
    # print(find_can_size(joe_needs), joe_needs)
    left += find_can_size(joe_needs) - joe_needs

print(left)
