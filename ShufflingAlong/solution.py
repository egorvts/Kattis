output = 0

def solution(inp):
    global output

    deck_size, shuffle_type = inp.split()
    deck_size = int(deck_size)
    deck = list(range(deck_size))

    if deck_size % 2 == 0:
        p1_len = deck_size // 2
    else:
        if shuffle_type == "out":
            p1_len = deck_size // 2 + 1
        else:
            p1_len = deck_size // 2

    def shuffle_deck(current_deck):
        global output
        p1, p2 = current_deck[:p1_len], current_deck[p1_len:]
        current_deck = []
        for i in range(max(len(p1), len(p2))):
            if shuffle_type == "out":
                if i == len(p2):
                    current_deck.append(p1[i])
                    break
                current_deck.append(p1[i])
                current_deck.append(p2[i])
            else:
                if i == len(p1):
                    current_deck.append(p2[i])
                    break
                current_deck.append(p2[i])
                current_deck.append(p1[i])

        output += 1
        return current_deck

    deck_copy = shuffle_deck(deck[:])
    while True:
        if deck_copy == deck:
            out = output
            output = 0
            return out
        deck_copy = shuffle_deck(deck_copy)

def test():
    assert solution("1 in") == solution("1 out") == 1
    assert solution("2 in") == 2
    assert solution("2 out") == 1
    assert solution("3 in") == solution("3 out") == 2
    assert solution("4 in") == 4
    assert solution("4 out") == 2

test()