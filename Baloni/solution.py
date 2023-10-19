n = int(input())
heights = list(map(int, input().split()))


def arrow(heights: list) -> list:
    heights_left = []
    balloon_0 = heights[0]

    for i in range(1, len(heights)):
        if heights[i] != balloon_0 - 1:
            heights_left.append(heights[i])
        else:
            balloon_0 -= 1

    return heights_left


@lambda _: _()
def tests():
    assert arrow([5, 4, 3, 1, 2]) == [1]
    assert arrow([4, 1, 3, 1]) == [1, 1]
    assert arrow([3, 2, 1]) == []
    assert arrow([4, 3, 3]) == [3]
    assert arrow([1]) == []
    print("Tests passed")


def solution(heights: list) -> int:
    count = 0

    while heights != []:
        heights = arrow(heights)
        count += 1

    return count


print(solution(heights))
