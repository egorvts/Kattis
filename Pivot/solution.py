_ = input()
nums = list(map(int, input().split()))


def solution(nums: list) -> int:
    outp = 0

    min_left = -1
    left_nums = set()
    for i in range(len(nums)):
        if nums[i] > min_left:
            min_left = nums[i]
            left_nums.add(nums[i])
    
    max_right = max(nums) + 1
    right_nums = set()
    for i in range(len(nums)-1, 0-1, -1):
        if nums[i] < max_right:
            max_right = nums[i]
            right_nums.add(nums[i])

    for i in left_nums:
        if i in right_nums:
            outp += 1

    return outp

print(solution(nums))