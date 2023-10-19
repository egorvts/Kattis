from sys import stdin

def get_code(l):
    code = 0
    if l in "BFPV": 
        code = 1
    elif l in "CGJKQSXZ":
        code = 2
    elif l in "DT":
        code = 3
    elif l == "L":
        code = 4
    elif l in "MN":
        code = 5
    elif l == "R":
        code = 6

    return code

for line in stdin:
    word = line[:-1]
    soundex = []
    for l in range(len(word)):
        code = get_code(word[l])
        if code == 0:
            continue
        elif (soundex and get_code(word[l-1]) != code) or not(soundex):
                soundex.append(str(code))

    print("".join(soundex))
            

