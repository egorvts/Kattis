commands = int(input())
cats = dict()
for c in range(commands):
    inp = input()
    if inp[0] == "0":
        cmd, cat, lvl = inp.split()
        cats[cat] = int(lvl)
    elif inp[0] == "1":
        cmd, cat, lvl = inp.split()
        cats[cat] += int(lvl)
    elif inp[0] == "2":
        cmd, cat = inp.split()
        cats.pop(cat)
    else:
        if cats == dict():
            print("The clinic is empty")
        else:
            max_lvl = max(cats.values())
            for c in cats:
                if cats[c] == max_lvl:
                    print(c)
                    break
