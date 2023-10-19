n = int(input())
buses = list(map(int, input().split()))
buses.sort()

short_form = []
start = buses[0]
finish = buses[0]
for i in range(n-1):
    if buses[i] + 1 == buses[i+1]:
        finish = buses[i+1]
    else:
        if finish - start >= 2:
            print(f"{start}-{finish}", end=" ")
        elif finish != start:
            print(start, finish, end=" ")
        else:
            print(start, end=" ")
        start = finish = buses[i+1]

if finish - start >= 2:
    print(f"{start}-{finish}", end=" ")
else:
    if start == finish:
        print(start, end=" ")
    else:
        print(start, finish, end=" ")

    
    