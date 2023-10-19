n = int(input())
heights = list(map(int, input().split()))


def solution(heights: list) -> int:
    arrows = []

    for height in heights:
        if height in arrows:
            arrows.remove(height)
            arrows.append(height-1)
        else:
            arrows.append(height-1)

    return len(arrows)


@lambda _: _()
def tests():
    assert solution([5, 4, 3, 1, 2]) == [1]
    assert solution([4, 1, 3, 1]) == [1, 1]
    assert solution([3, 2, 1]) == []
    assert solution([4, 3, 3]) == [3]
    assert solution([1]) == []
    print("Tests passed")


print(solution(heights))
