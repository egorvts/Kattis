from sys import stdin
count = 0
for line in stdin:
    n = line[0]
    nums = list(map(int, line[1:].split()))
    count += 1
    print(f"Case {count}: {min(nums)} {max(nums)} {max(nums) - min(nums)}")
    