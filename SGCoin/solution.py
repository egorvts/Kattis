from string import ascii_lowercase

def H(previous_hash, transaction, token):
    v = previous_hash
    for i in range(len(transaction)):
        v = (v * 31 + ord(transaction[i])) % 1000000007
    return (v * 7 + token) % 1000000007


# hash = int(input())
print(H(140000000, "alice-pays-bob-3-sg-coins", 306969470))

def generate_str():
    

d = dict()
for i in range(1, 100):
    h = i * 10 ** 7
    for j in range(100):
        # for l in [chr(i) for i in range(1000)]:
        for l1 in "-0123456789" + ascii_lowercase:
            for l2 in "-0123456789" + ascii_lowercase:
                new_hash = H(h, l1+l2, j)
                if new_hash % 10 ** 7 == 0:
                    d[i * 10 ** 7] = [new_hash, l1+l2, j]

print(d)