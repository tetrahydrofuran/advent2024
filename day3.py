import re


def mul(x, y):
    return x * y


def evaluate_instructions(valid_instructions):
    do = True
    total = 0
    for i in valid_instructions:
        if i[0] == '':
            if i[1] == '':
                do = True
            else:
                do = False
        else:
            total += eval(i[0]) * do
    return total


with open('input/day3.txt') as f:
    t = f.read()


pattern = r'mul\(\d+,\d+\)'

total = 0

valid_instructions = re.findall(pattern, t)
total += sum([eval(i) for i in valid_instructions])
print('Part 1:', total)

total2 = 0
pattern2 = r"(mul\(-?\d+,-?\d+\))|(don't\(\))|(do\(\))"
valid_instructions = re.findall(pattern2, t)
total2 += evaluate_instructions(valid_instructions)
print('Part 2:', total2)