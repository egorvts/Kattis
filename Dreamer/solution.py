from itertools import permutations


def is_leap(year):
    if year % 400 == 0:
        return True
    elif year % 100 == 0:
        return False
    elif year % 4 == 0:
        return True
    else:
        return False


def is_valid(date):
    day = int(date[0:2])
    month = int(date[2:4])
    year = int(date[4:])
    if year >= 2000:
        if (1 <= month) and (month <= 12):
            if month == 2:
                return ((1 <= day) and (day <= 28)) or ((day == 29) and is_leap(year))
            else:
                if month in [1, 3, 5, 7, 8, 10, 12]:
                    return (1 <= day) and (day <= 31)
                else:
                    return (1 <= day) and (day <= 30)
        else:
            return False
    else:
        return False

def compare(date1, date2):
    day1, month1, year1 = date1[0:2], date1[2:4], date1[4:]
    day2, month2, year2 = date2[0:2], date2[2:4], date2[4:]
    if year1 > year2:
        return 1
    elif year1 == year2:
        if month1 > month2:
            return 1
        elif month1 == month2:
            if day1 > day2:
                return 1
            elif day1 == day2:
                return 0
            else:
                return -1
        else:
            return -1
    else:
        return -1


for t in range(int(input())):
    nums = list(input())
    nums.remove(" ")
    nums.remove(" ")
    variants = set(map("".join, permutations(nums)))

    count = 0

    first_date = "9" * 8

    for v in variants:
        if is_valid(v):
            count += 1
            if compare(first_date, v) == 1:
                first_date = v

    if count == 0:
        first_date = ""

    print(count, first_date[0:2], first_date[2:4], first_date[4:])
