n = int(input())
papers = list(map(int, input().split()))


def paper_size(f):
    if f % 2 == 0:
        return (2 ** (-3/4) / 2 ** (f / 2 - 1), 2 ** (-5/4) / 2 ** (f / 2 - 1))
    else:
        even_size = paper_size(f-1)
        return (even_size[1], even_size[0] / 2)


res = 0
i = 0
papers_needed = 2
while i < n - 1:
    if papers[i] == 0:
        papers_needed *= 2
    elif papers[i] >= papers_needed:
        s = paper_size(i+2)
        if papers_needed == 2:
            res += s[0]
        else:
            res += ((papers_needed - 2) * s[0]) + ((papers_needed / 2) * s[1])
            print(papers_needed, (papers_needed - 2), (papers_needed / 2))
        break
    elif (i == n-2) and papers[i] < papers_needed:
        res = 0
        break
    else:
        s = paper_size(i+2)
        res += s[0]
    i += 1

if res:
    print(res)
else:
    print("impossible")

# print(paper_size(2))
# print(paper_size(3))
# print(paper_size(4))
