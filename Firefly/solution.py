from bisect import bisect_right, bisect_left

n, h = map(int, input().split())

stalagmites = []
stalactites = []
for i in range(n):
    if i % 2 == 0:
        stalagmites.append(int(input()))
    else:
        stalactites.append(int(input()))

stalagmites.sort()
stalactites.sort()

def find_h(height):
    i_g = bisect_right(stalagmites, height)
    # print(height, stalagmites, stalagmites[i_g:])
    i_c = bisect_left(stalactites, h - height)
    # print(h - height, stalactites, stalactites[i_c:])
    # return len(stalagmites[i_g:]) + len(stalactites[i_c:])
    return int(n/2) - i_g + int(n/2) - i_c

heights = []
for height in range(h):
    heights.append(find_h(height))

print(min(heights), heights.count(min(heights)))