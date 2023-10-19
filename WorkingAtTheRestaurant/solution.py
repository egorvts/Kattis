while True:
    n = int(input())
    if n == 0:
        break
            
    pile1 = 0
    pile2 = 0
    for i in range(n):
        operation, m = input().split()
        m = int(m)
        if operation == "DROP":
            pile2 += m
            print(f"DROP 2 {m}")
        else:
            if pile1 >= m:
                pile1 -= m
                print(f"TAKE 1 {m}")
            else:
                if pile1 > 0:
                    print(f"TAKE 1 {pile1}")
                    m -= pile1
                    pile1 = 0
                    print(f"MOVE 2->1 {pile2}")
                    pile1 = pile2 - m
                    pile2 = 0
                    print(f"TAKE 1 {m}")
                else:
                    print(f"MOVE 2->1 {pile2}")
                    pile1 += pile2
                    pile2 = 0
                    print(f"TAKE 1 {m}")
                    pile1 -= m
    print()

