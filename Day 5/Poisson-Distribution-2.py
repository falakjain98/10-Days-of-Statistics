import math
a = input()
nums=[]
for i in a.split(' '):
    nums.append(float(i))
l1 = nums[0]
l2 = nums[1]
print(round(160 + 40*(l1+l1**2),3))
print(round(128 + 40*(l2+l2**2),3))