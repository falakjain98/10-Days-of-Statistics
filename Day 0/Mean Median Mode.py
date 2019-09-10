 # Enter your code here. Read input from STDIN. Print output to STDOUT
n = int(input())
a = input()
nums=[]
for i in a.split(' '):
   nums.append(int(i))

import numpy as np
from scipy import stats
nums = np.array(nums)
print(np.mean(nums))
print(np.median(nums))
print(int(stats.mode(nums)[0]))
