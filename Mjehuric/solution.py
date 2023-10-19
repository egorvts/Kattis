seq = list(map(int, input().split()))

def swap(seq, i):
    seq[i], seq[i+1] = seq[i+1], seq[i]
    return seq

count = 0
while seq != [1, 2, 3, 4, 5]:
    if seq[count] > seq[count+1]:
        print(*swap(seq, count))

    if count == 3:
        count = 0
    else:
        count += 1
