inp = list(input())

def solution(sequence):
    # Up
    result = sequence.count("D") * 2
    if sequence[0] == "D":
        result += 1
    print(result)
    # Down
    result = sequence.count("U") * 2 - 2
    if sequence[0] == "U" and sequence[1] == "D":
        result += 1
    elif sequence[0] == "U" and sequence[1] == "U":
        result -= 1
    print(result)
    # Prefered
    result = 0
    for i in range(len(sequence)-1):
        if sequence[i] != sequence[i+1]:
            result += 1
    print(result)

solution(inp)