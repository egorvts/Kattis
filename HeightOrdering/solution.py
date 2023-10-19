for _ in range(int(input())):
    inp = list(map(int, input().split()))
    k, heights = inp[0], inp[1:]

    max_height = 0
    

    steps = 0
    for i in range(20):
        if heights[i] < heights[max_height]:
            steps_to_take = 0
            for j in range(len(heights[:i])):
                if heights[j] > heights[i]:
                    steps_to_take += 1
            steps += steps_to_take
        else:
            max_height = i

    print(k, steps)
