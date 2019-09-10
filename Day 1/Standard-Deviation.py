# Enter your code here. Read input from STDIN. Print output to STDOUT
import math
n = int(input())
a = input()
nums=[]
for i in a.split(' '):
    nums.append(int(i))
mean = sum(nums)/n
sqd = []
for i in range(n):
    sqd.append((nums[i] - mean)**2)
sigma = round(math.sqrt(sum(sqd)/n),1)
print(sigma)