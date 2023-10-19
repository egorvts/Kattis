from sys import stdin

vars = {}
vs = ["unknown"] * 3000
for line in stdin:
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
            num1 = acc
            num2 = vars[line[i*2 + 2]]

            if op == "+":
                acc += num2
            else:
                acc -= num2

        print(" ".join(line), "=", vs[acc])
