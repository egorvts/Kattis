combos = dict()
diff_combos = []

max_combo = 0
for i in range(int(input())):
    courses = list(input().split())
    courses.sort()
    courses_key = "".join(courses)
    if courses_key in combos:
        combos[courses_key] += 1
    else:
        combos[courses_key] = 1
    if combos[courses_key] > max_combo:
        max_combo = combos[courses_key]

res = 0
for c in combos.values():
    if c == max_combo:
        res += c

print(res)