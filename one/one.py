from collections import Counter

f = open("in.txt")

left = []
right = []
total_diff = 0

for line in f.readlines():
    nums = line.split()
    
    left.append(int(nums[0]))
    right.append(int(nums[1]))

left.sort()
right.sort()

for i in range(len(left)):
    total_diff += abs(left[i] - right[i])

print("pt 1", total_diff)

r_counts = Counter(right)

sim_score = 0

for num in left:
    if num in r_counts:
        sim_score += num * r_counts[num]

print("pt 2", sim_score)
