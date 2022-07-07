# https://www.w3resource.com/python-exercises/puzzles/index.php

# 1

def finding(liste):
    nineteen = 0
    five = 0
    for i in liste:
        if i == 19:
            nineteen += 1
            if nineteen == 2:
                continue
        if i == 5:
            five += 1
    if (nineteen == 2) and (five >= 3):
        return True
    else:
        return False


print(finding([19, 19, 15, 5, 3, 5, 5, 2]))

# 2


def check(liste):
    length = len(liste)
    element = liste[4]
    count_element = 0
    for i in liste:
        if i == element:
            count_element += 1
    if (count_element == 3) and (length == 8):
        return True
    else:
        return False


print(check([19, 15, 11, 7, 5, 6, 2]))

# 3


def ask(num):
    if (num > (4**4) and (num % 34 == 4)):
        return True
    else:
        return False


print(ask(854))
