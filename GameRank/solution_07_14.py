matches = list(input())


def solution(matches: list):
    current_rank = 25
    current_stars = 0
    win_streak = 0

    for match in matches:
        if match == "W":
            win_streak += 1

            if current_rank > 20:
                if current_stars == 2:
                    if win_streak >= 3:
                        current_rank -= 1
                        current_stars = 2
                    else:
                        current_rank -= 1
                        current_stars = 1
                elif current_stars == 1:
                    if win_streak >= 3:
                        current_rank -= 1
                        current_stars = 1
                    else:
                        current_stars += 1
                else:
                    if win_streak >= 3:
                        current_stars += 2
                    else:
                        current_stars += 1

            elif current_rank > 15:
                if current_stars == 3:
                    if win_streak >= 3:
                        current_rank -= 1
                        current_stars = 2
                    else:
                        current_rank -= 1
                        current_stars = 1
                elif current_stars == 2:
                    if win_streak >= 3:
                        current_rank -= 1
                        current_stars = 1
                    else:
                        current_stars += 1
                else:
                    if win_streak >= 3:
                        current_stars += 2
                    else:
                        current_stars += 1

            elif current_rank > 10:
                if current_stars == 4:
                    if win_streak >= 3:
                        current_rank -= 1
                        current_stars = 2
                    else:
                        current_rank -= 1
                        current_stars = 1
                elif current_stars == 3:
                    if win_streak >= 3:
                        current_rank -= 1
                        current_stars = 1
                    else:
                        current_stars += 1
                else:
                    if win_streak >= 3:
                        current_stars += 2
                    else:
                        current_stars += 1

            elif current_rank > 5:
                if current_stars == 5:
                    if win_streak >= 3:
                        current_rank -= 1
                        current_stars = 2
                    else:
                        current_rank -= 1
                        current_stars = 1
                elif current_stars == 4:
                    if win_streak >= 3:
                        current_rank -= 1
                        current_stars = 1
                    else:
                        current_stars += 1
                else:
                    if win_streak >= 3:
                        current_stars += 2
                    else:
                        current_stars += 1

            elif current_rank > 0:
                if current_stars == 5:
                    current_rank -= 1
                    current_stars = 1
                else:
                    current_stars += 1
            
            elif current_rank < 0:
                return "Legend"


        else:
            win_streak = 0
            if current_rank < 20 or (current_rank == 20 and current_stars != 0):
                if current_stars != 0:
                    current_stars -= 1
                else:
                    if current_rank > 15:
                        current_rank += 1
                        current_stars = 2
                    elif current_rank > 10:
                        current_rank += 1
                        current_stars = 3
                    else:
                        current_rank += 1
                        current_stars = 4

    return current_rank


print(solution(matches))
