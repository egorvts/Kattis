def insert(num, lst):
    for i in range(len(lst)):
        if lst[i] > num:
            return lst[:i] + [num] + lst[i+1:]   
    return lst + [num]

def insert_reverse(num, lst):
    for i in range(len(lst)-1, -1, -1):
        if lst[i] > num:
            return lst[:i+1] + [num] + lst[i+1:]
    
    return [num] + lst

nums1 = []
nums2 = []

for i in range(int(input())):
    n1, n2 = map(int, input().split())

    if i == 0:
        nums1.append(n1)
        nums2.append(n2)
    else:
        nums1 = insert(n1, nums1)
        nums2 = insert_reverse(n2, nums2)

    # print(nums1, nums2)

    max_sum = 0
    for i in range(len(nums1)):
        max_sum = max(nums1[i] + nums2[i], max_sum)
    
    print(max_sum)
