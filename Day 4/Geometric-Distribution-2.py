# Enter your code here. Read input from STDIN. Print output to STDOUT
import math
a = input()
b = int(input())
nums = []
for i in a.split(' '):
    nums.append(int(i))
p = nums[0]/nums[1]
prob = 0
for i in range(1,b+1):
    prob = prob + (p * ((1-p)**(i-1)))
print(round(prob,3))