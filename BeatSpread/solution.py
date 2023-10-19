def game(scores, difference):
    if scores < difference:
        print("impossible")
        return
    
    x = (scores - difference) // 2
    y = x + difference

    if (x + y != scores) or (abs(x - y) != difference):
        print("impossible")
        return

    print(max(x, y), min(x, y)) 

for _ in range(int(input())):
    scores, difference = map(int, input().split())
    # print(scores, difference)
    game(scores, difference)
