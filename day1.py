from collections import Counter


list1 = []
list2 = []

with open('input/day1.txt') as f:
    t = f.readlines()

for i in t:
    j = i.strip().split(' ')
    list1.append(int(j[0]))
    list2.append(int(j[-1]))

list1 = sorted(list1)
list2 = sorted(list2)

distance = 0
for a, b in zip(list1, list2):
    distance += abs(a - b)

print('Part 1:', distance)


c = Counter(list2)
sim = 0

for i in list1:
    sim += i * c[i]

print('Part 2:', sim)