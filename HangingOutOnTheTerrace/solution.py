limit, events = map(int, input().split())

people_count = 0
not_allowed = 0

for i in range(events):
    eve, cou = input().split()
    cou = int(cou)
    if eve == "enter":
        if people_count + cou <= limit:
            people_count += cou
        else:
            not_allowed += 1
    else:
        people_count -= cou

print(not_allowed)
