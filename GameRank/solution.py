def solution(inp: str) -> int:
    sequence = [*inp]
    current_rank = 25
    current_stars = 0
    win_streak = 0

    for game in sequence:
        if game == "L" and current_rank != "Legend":
            win_streak = 0
            if current_rank > 20 or (current_rank == 20 and current_stars == 0):
                continue
            if current_stars != 0:
                current_stars -= 1
                continue
            else:
                current_rank -= 1
                if current_rank >= 21:
                    current_stars = 1
                elif current_rank >= 16:
                    current_stars = 2
                elif current_rank >= 11:
                    current_stars = 3
                else:
                    current_stars = 4
        elif game == "L":
            win_streak = 0
            continue
        elif game == "W":
            if win_streak >= 3:
                current_stars += 1
            if current_stars == 2 and current_rank >= 21:
