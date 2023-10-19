import copy


def isSequence(seq: list) -> bool:
    seq.sort()
    return (seq[3] - seq[2]) == (seq[2] - seq[1]) == (seq[1] - seq[0])


nums = list(map(int, input().split()))[:3]
nums.sort()

step = min(nums[2] - nums[1], nums[1] - nums[0])

for i in range(0, len(nums)):
    potentialSequence = copy.copy(nums) + [nums[i] + step]
    if isSequence(potentialSequence):
        print(nums[i] + step)
        break
