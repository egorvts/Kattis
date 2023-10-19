from sys import stdin
from random import randint
from string import ascii_lowercase

def generate_calc(names):
    calc = []
    for i in range(randint(1, len(names)-1)):
        calc.append(names[randint(0, len(names)-1)])
        if i != len(names)-1:
            calc.append("+-"[randint(0, 1)])

    return " ".join(calc)

def oracle():
    inp = []
    names = []
    for _ in range(5):
        letters = ascii_lowercase
        name = "".join([letters[randint(0, 25)] for i in range(randint(1, 5))])
        names.append(name)

    for i in range(20):
        if randint(0, 1):
            inp.append(f"def {names[randint(0, len(names)-1)]} {randint(-2, 2)}")

    for i in range(10):
        inp.append(f"calc {generate_calc(names)}")

    return inp

def solution(inp):
    print("\n".join(inp))
    print()
    vars = {}
    vs = ["unknown"] * 3000
    for line in inp:
        # print("l", line)
        line = list(line.rstrip().split())
        cmd = line[0]
        if cmd == "def":
            name = line[1]
            value = int(line[2])
            if name in vars:
                vs[vars[name]] = "unknown"
            vars[name] = value
            vs[value] = name
        elif cmd == "clear":
            vars = {}
            vs = ["unknown"] * 3000
        else:
            line = line[1:-1] # remove calc and "="
            if not all([(line[i] in vars) for i in range(0, len(line), 2)]):
                print(" ".join(line), "=", "unknown")
                continue
            acc = vars[line[0]]
            for i in range((len(line)-1)//2):
                op = line[i*2 + 1]
                num2 = vars[line[i*2 + 2]]

                if op == "+":
                    acc += num2
                else:
                    acc -= num2

            print(" ".join(line), "=", vs[acc])

for _ in range(100):
    solution(oracle())