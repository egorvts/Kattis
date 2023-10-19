while True:
    s0, s1, r0, r1 = map(int, input().split())
    if s0 == s1 == r0 == r1 == 0:
        break
    else:
        sIsHighest = (s0, s1) == (1, 2) or (s0, s1) == (2, 1)
        rIsHighest = (r0, r1) == (1, 2) or (r0, r1) == (2, 1)
        if sIsHighest and rIsHighest:
            print("Tie.")
        elif sIsHighest:
            print("Player 1 wins.")
        elif rIsHighest:
            print("Player 2 wins.")
        else:
            sIsDoubles = s0 == s1
            rIsDoubles = r0 == r1
            if sIsDoubles and rIsDoubles:
                if s0 > r0:
                    print("Player 1 wins.")
                elif s0 < r0:
                    print("Player 2 wins.")
                else:
                    print("Tie.")
            elif sIsDoubles:
                print("Player 1 wins.")
            elif rIsDoubles:
                print("Player 2 wins.")
            else:
                if int((str(max(s0, s1)) + str(min(s0, s1)))) == int((str(max(r0, r1)) + str(min(r0, r1)))):
                    print("Tie.")
                elif int((str(max(s0, s1)) + str(min(s0, s1)))) > int((str(max(r0, r1)) + str(min(r0, r1)))):
                    print("Player 1 wins.")
                else:
                    print("Player 2 wins.")
