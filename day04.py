with open('input/day04.txt') as f:
    t = f.read()
arr = [list(i) for i in t.split('\n')]

# get all combinations of -1, 0, 1
directions = []
for i in (-1, 0, 1):
    for j in (-1, 0, 1):
        if i == 0 and j == 0:
            continue
        directions.append((i, j))

DEPTH = {1: 'M', 2: 'A', 3: 'S'}

def check(r, c, direction, depth):
    try:
        rn = r + direction[0]
        cn = c + direction[1]
        if rn < 0 or cn < 0:
            return False
        v = arr[rn][cn]

        if v == DEPTH[depth]:
            if depth == 3:
                return True
            else:
                return check(rn, cn, direction, depth+1)
        else:
            return False
    except:
        return False

def check_all(r, c):
    xm = 0
    for d in directions:
        x = check(r, c, d, 1)
        xm += x
    return xm

def check_mas(r, c):
    r1, c1 = r - 1, c - 1
    r2, c2 = r + 1, c + 1
    r3, c3 = r - 1, c + 1
    r4, c4 = r + 1, c - 1
    coords = (r1, c1, r2, c2, r3, c3, r4, c4)
    if any(i < 0 for i in coords):
        return False  # Out of bounds, can't complete
    try:
        if (
            (arr[r1][c1] == 'S' and arr[r2][c2] == 'M') or
            (arr[r2][c2] == 'S' and arr[r1][c1] == 'M')
        ) and (
            (arr[r3][c3] == 'S' and arr[r4][c4] == 'M') or
            (arr[r4][c4] == 'S' and arr[r3][c3] == 'M')
        ):
            return True
        return False
    except:
        return False
    

xmas = 0
for row, rval in enumerate(arr):
    for col, val in enumerate(rval):
        if val == 'X':
            xmas += check_all(row, col)
print('Part 1:', xmas)

mas = 0
for row, rval in enumerate(arr):
    for col, val in enumerate(rval):
        if val == 'A':
            mas += check_mas(row, col)
print('Part 2:', mas)