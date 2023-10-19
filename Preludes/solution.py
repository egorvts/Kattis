from sys import stdin

letters = "ABCDEFGA"
case_num = 1
for line in stdin:
    name, tonality = line.split()
    if len(name) == 1:
        print(f"Case {case_num}: UNIQUE")
    elif name[0] == "A" and name[1] == "b":
        print(f"Case {case_num}: G# {tonality}")
    elif name[1] == "#":
        print(f"Case {case_num}: {letters[letters.index(name[0])+1]}b {tonality}")
    else:
        print(f"Case {case_num}: {letters[letters.index(name[0])-1]}# {tonality}")

    case_num += 1
