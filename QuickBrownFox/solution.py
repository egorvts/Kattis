from sys import stdin
from string import ascii_lowercase

letters = ascii_lowercase

for t in range(int(input())):
    letters_in = [0] * 26
    inp = stdin.readline()[:-1]
    for i in inp:
        i = ord(i)
        if 97 <= i <= 122:
            letters_in[i-97] += 1
        elif 65 <= i <= 90:
            letters_in[i-65] += 1
    if all(letters_in):
        print("pangram")
    else:
        print("missing ", end="")
        for i in range(26):
            if letters_in[i] == 0:
                print(letters[i], end="")
        print()
