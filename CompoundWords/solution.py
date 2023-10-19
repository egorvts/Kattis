from sys import stdin

words = set()
for line in stdin:
    ws = line[:-1].split()
    for w in ws:
        words.add(w)

combs = set()
for word in words:
    for w in words:
        if word != w:
            combs.add(word + w)
            combs.add(w + word)

print("\n".join(sorted(combs)))