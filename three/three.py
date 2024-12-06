import re

f = open("test.txt")
mul_pattern = re.compile('mul\(\d+,\d+\)')
do_pattern = re.compile('do\(\)')
dont_pattern = re.compile('don\'t\(\)')

total = 0
do_mul = True

for line in f.readlines():
    for m in re.finditer(mul_pattern, line):
        a, b = m.strip("mul").strip("(").strip(")").split(",")
        total += int(a) * int(b)

print("pt 2", total)
