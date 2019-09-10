# Enter your code here. Read input from STDIN. Print output to STDOUT
import math
a = input()
b = int(input())
nums = []
for i in a.split(' '):
    nums.append(int(i))
p = nums[0]/nums[1]
prob = ((1-p)**(b-1))*(p)
print(round(prob,3))