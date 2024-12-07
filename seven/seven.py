import numpy as np


def eval(ans, nums, t_code):
    # b_code -> 0 == mul, 1 == add
    running_tot = nums[0]
    for i in range(1, len(nums)):
        if i - 1 >= len(t_code) or t_code[i-1] == "0":
            running_tot *= nums[i]
        elif t_code[i-1] == "1":
            running_tot += nums[i]
        elif t_code[i-1] == "2":
            running_tot = int(str(running_tot) + str(nums[i]))
    if running_tot == ans:
        return True
    return False


def check(ans, nums):
    for i in range(3 ** (len(nums) - 1)):
        '''print(ans, nums, i, bin(i), bin(i)
                  .replace("0b", "")
                  .replace("0", "* ")
                  .replace("1", "+ "))'''
        if eval(ans, nums, np.base_repr(i, base=3)[::-1]):
            '''print(ans, nums, i, bin(i).replace("0b", ""), bin(i)
                  .replace("0b", "")
                  .replace("0", "* ")
                  .replace("1", "+ "))'''
            return True
    return False


f = open("in.txt")
total = 0
n = 0
t = 0
for line in f.readlines():
    t += 1
    a_str, num_str = line.split(":")
    ans = int(a_str)
    nums = [int(x) for x in num_str.strip('\n').strip().split(" ")]
    if check(ans, nums):
        n += 1
        total += ans

print("pt1:", total)
print(n, "good of", t)
