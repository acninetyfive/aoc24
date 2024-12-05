f = open("in.txt")

safe = 0

unsafe = []


def check_safe(report):
    inc = None
    for i in range(1, len(report)):
        if inc is None:
            inc = True if report[1] > report[0] else False
        diff = report[i] - report[i-1]
        if abs(diff) < 1 or abs(diff) > 3:
            return False
        if inc is True and diff < 0:
            return False
        if inc is False and diff > 0:
            return False
    return True


for line in f.readlines():
    report = [int(x) for x in line.split()]
    if check_safe(report):
        safe += 1
    else:
        unsafe.append(report)

print("pt 1", safe)

for r in unsafe:
    for i in range(len(r)):
        if check_safe([r[x] for x in range(len(r)) if x != i]):
            safe += 1
            break

print("pt 2", safe)