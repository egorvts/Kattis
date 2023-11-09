from sys import stdin

case = 1
while True:
    inp = stdin.readline()
    if inp:
        print(f"Case {case}:")
        nums = []

        n = int(inp)
        for i in range(n):
            nums.append(int(stdin.readline()))
        nums.sort()

        sums = []
        for i in nums:
            for j in nums:
                if i != j:
                    sums.append(i + j)
        sums.sort()

        m = int(stdin.readline())
        # print(sums)
        for i in range(m):
            query = int(stdin.readline())
            closest = 0
            for s in range(len(sums)):
                if sums[s] > query:
                    if s == 0:
                        closest = sums[0]
                    else:
                        if query - sums[s-1] < sums[s] - query:
                            closest = sums[s-1]
                        else:
                            closest = sums[s]
                    break
            else:
                closest = sums[-1]
                
            print(f"Closest sum to {query} is {closest}.")
        case += 1
    else:
        break


        