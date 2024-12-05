from functools import cmp_to_key, reduce
import graphlib

f = open("in.txt")

rules = {}
updates = []

line = f.readline()
while line != '\n':
    x, y = [int(n) for n in line.split("|")]

    if x not in rules:
        rules[x] = set()
    if y not in rules:
        rules[y] = set()

    rules[y].add(x)

    line = f.readline()


line = f.readline()
good_updates = []
bad_updates = []
while line:
    update = [int(n) for n in line.split(",")]

    disallowed = set()

    i = 0
    good = True
    while i < len(update) and good:
        if update[i] in disallowed:
            good = False
        else:
            disallowed.add(update[i])
            disallowed = disallowed.union(rules[update[i]])
        i += 1
    if good:
        good_updates.append(update)
    else:
        bad_updates.append(update)

    line = f.readline()

middle_sums = 0
for u in good_updates:
    middle_sums += u[(len(u) - 1)//2]

print("pt 1:", middle_sums)

#ts = graphlib.TopologicalSorter(rules)
#ordered_nums = list(ts.static_order())


def compare(left, right):
    if right in rules[left]:
        return 1
    elif left in rules[right]:
        return -1
    return 0


middle_sums = 0
for u in bad_updates:
    u.sort(key=cmp_to_key(compare))
    middle_sums += u[(len(u) - 1)//2]

print("pt 2:", middle_sums)
