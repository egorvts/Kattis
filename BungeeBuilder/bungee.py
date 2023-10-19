n = int(input())
heights = list(map(int, input().split()))

max_height = max(heights)
max_height_ind = []

second_height = 0
second_height_ind = []
for i in range(n):
    if heights[i] == max_height:
        max_height_ind.append(i)
    elif max_height > heights[i] > second_height:
        second_height = heights[i]

for i in range(n):
    if heights[i] == second_height:
        second_height_ind.append(i)


max_diff = 0
ind = 0

for el1 in max_height_ind:
    for el2 in max_height_ind + second_height_ind:
        if el1 != el2:
            h1 = heights[el1]
            h2 = heights[el2]
            min_h = min(h1, h2)
            min_in, min_ind = min_h, 0
            # if all(map(lambda x: x < min_h, heights[el1+1:el2])):
            for i in range(min(el1, el2)+1, max(el1, el2)):
                if heights[i] < min_in:
                    min_in = heights[i]
                    min_ind = i

            diff = min_h - min_in
            if diff > max_diff:
                max_diff = diff
                ind = min_ind


