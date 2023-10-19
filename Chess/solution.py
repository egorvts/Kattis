LETTERS = "ABCDEFGH"

def solution(inp: str) -> str:
    x1, y1, x2, y2 = inp.split()
    x1, x2 = LETTERS.index(x1) + 1, LETTERS.index(x2) + 1
    y1, y2 = int(y1), int(y2)

    # No move
    if (x1 == x2) and (y1 == y2):
        return f"0 {LETTERS[x1-1]} {y1}"

    # Impossible
    #if (x1 + y1) % 2 != (x2 + y2) % 2:
        #return "Impossible"
    if (x1 % 2 != 0 and y1 % 2 != 0) or (x1 % 2 == 0 and y1 % 2 == 0):
        if not ((x2 % 2 != 0 and y2 % 2 != 0) or (x2 % 2 == 0 and y2 % 2 == 0)):
            return "Impossible"
    elif (x1 % 2 != 0 and y1 % 2 == 0) or (x1 % 2 == 0 and y1 % 2 != 0):
        if not ((x2 % 2 != 0 and y2 % 2 == 0) or (x2 % 2 == 0 and y2 % 2 != 0)):
            return "Impossible"
    
    # One move
    if abs(x2 - x1) == abs(y2 - y1):
        return f"1 {LETTERS[x1-1]} {y1} {LETTERS[x2-1]} {y2}"
    
    # Two moves
    for x3 in range(1, 8+1):
        for y3 in range(1, 8+1):
            if (abs(x3 - x1) == abs(y3 - y1)) and (abs(x3 - x2) == abs(y3 - y2)):
                return f"2 {LETTERS[x1-1]} {y1} {LETTERS[x3-1]} {y3} {LETTERS[x2-1]} {y2}"

def test():
    assert solution("E 2 E 3") == "Impossible"
    assert solution("F 1 E 8") == "2 F 1 B 5 E 8"
    assert solution("H 1 A 8") == "1 H 1 A 8"
    assert solution("A 3 A 3") == "0 A 3"

test()

for test in range(int(input())):
    print(solution(input()))

