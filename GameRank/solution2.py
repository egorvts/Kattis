matches = list(input())


def max_stars(rank: int) -> int:
    if rank > 20:
        return 2
    elif rank > 15:
        return 3
    elif rank > 10:
        return 4
    return 5


@lambda _: _()
def tests():
    assert max_stars(20) == 3
    assert max_stars(5) == 5


def solution(matches: list):
    current_rank = 25
    current_stars = 0
    win_streak = 0

    for match in matches:
        if match == "W":
            win_streak += 1
            stars_to_add = 1

            if current_rank > 5 and win_streak >= 3:
                stars_to_add += 1

            if current_rank > 20:
                if current_stars + stars_to_add > 2:
                    current_rank -= 1
                    current_stars = current_stars + stars_to_add - 2
                else:
                    current_stars += stars_to_add

            elif current_rank > 15:
                if current_stars + stars_to_add > 3:
                    current_rank -= 1
                    current_stars = current_stars + stars_to_add - 3
                else:
                    current_stars += stars_to_add

            elif current_rank > 10:
                if current_stars + stars_to_add > 4:
                    current_rank -= 1
                    current_stars = current_stars + stars_to_add - 4
                else:
                    current_stars += stars_to_add

            elif current_rank > 0:
                if current_stars + stars_to_add > 5:
                    current_rank -= 1
                    current_stars = current_stars + stars_to_add - 5
                else:
                    current_stars += stars_to_add

            elif current_rank == 1 and current_stars == 4:
                return "Legend"

        else:
            win_streak = 0

            if current_rank > 0 and current_rank < 20 or (current_rank == 20 and current_stars != 0):
                if current_stars != 0:
                    current_stars -= 1
                else:
                    current_rank += 1
                    current_stars = max_stars(current_rank) - 1

    return current_rank


result = solution(matches)
if result > 0:
    print(result)
else:
    print("Legend")
