def mid(u):
    return u[len(u) // 2 ]

def is_good_update(u):
    for i, v in enumerate(u[1:]):  # Skip first check since nothing before
        bad = set(u[:i+1]).intersection(before_after.get(v,set()))
        if len(bad) != 0:
            return False
    return True

# Part 2 Functions
def realign(u, v, bad):
    early = min([u.index(b) for b in bad])
    second = u[early:]
    second.remove(v)
    return u[:early] + [v] + second

def check(u):
    for i, v in enumerate(u[1:]):
        bad = set(u[:i+1]).intersection(before_after.get(v,set()))
        if len(bad) != 0:
            return  v, bad
    return v, bad


# region Input Setup
with open('input/day05.txt') as f:
    t = f.readlines()


before_after = {}
updates = []
for i in t:
    if '|' in i:
        b, a = [int(j) for j in i.split('|')]
        if b not in before_after.keys():
            before_after[b] = {a}
        else:
            before_after[b].add(a)
    if ',' in i:
        updates.append([int(j) for j in i.split(',')])
# endregion

bad_updates = []

total = 0
for u in updates:
    g = is_good_update(u)
    if g:
        total += mid(u)
    else:
        bad_updates.append(u)
print('Part1:', total)


total2 = 0
for u in bad_updates:
    good = False
    while not good:
        v, bad = check(u)
        good = len(bad) == 0
        if good:
            break
        u = realign(u, v, bad)
    total2 += mid(u)    
print('Part2:', total2)
