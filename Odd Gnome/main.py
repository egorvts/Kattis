for _ in range(int(input())):
    ind = 1
    inp = list(map(int, input().split()))
    gnomesCount = inp[0]
    gnomes = inp[1:]
    for i in range(len(gnomes)):
        if gnomes[ind] - gnomes[ind - 1] != 1:
            print(ind + 1)
            break
        else:
            ind += 1


