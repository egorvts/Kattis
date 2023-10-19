_ = input()
nums = list(map(int, input().split()))


def solution(nums: list) -> int:
    outp = 0
    for i in range(len(nums)):
        num = nums[i]
        nums_before = nums[:i]
        nums_after = nums[i+1:]
        if all(map(lambda x: x <= num, nums_before)) and all(map(lambda x: x > num, nums_after)):
            outp += 1
    return outp


print(solution(nums))
