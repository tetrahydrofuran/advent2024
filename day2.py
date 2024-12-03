from copy import copy


def level_safe(l):
    diffs = []
    for a, b in zip(l, l[1:]):
        diffs.append(a - b)

    a, b = min(diffs), max(diffs)
    if a * b < 1:
        return False

    a, b = abs(a), abs(b)
    mind, maxd = min(a, b), max(a, b)
    if mind > 3 or maxd > 3:
        return False
    return True

def level_safe_damped(l):
    """
    Stupid brute force method vs trying to identify the problem.
    """
    s = level_safe(l)
    if not s:
        for i in range(len(l)):
            j = copy(l)
            j.pop(i)
            if level_safe(j):
                return True
    return s


with open('input/day2.txt') as f:
    t = f.readlines()

levels = []
for i in t:
    levels.append([int(j) for j in i.strip().split(' ')])

safe = [level_safe(i) for i in levels]
print('Part 1:', sum(safe))
safe2 = [level_safe_damped(i) for i in levels]
print('Part 2:', sum(safe2))
