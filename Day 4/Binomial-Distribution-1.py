# Enter your code here. Read input from STDIN. Print output to STDOUT
import math
a = input()
nums=[]
for i in a.split(' '):
    nums.append(float(i))
sums=sum(nums)
nums[0]=nums[0]/sums
nums[1]=nums[1]/sums
p1 = ((math.factorial(6)/(math.factorial(3)*math.factorial(3)))*((nums[0])**3)*(nums[1]**3)) + ((math.factorial(6)/(math.factorial(2)*math.factorial(4)))*((nums[0])**4)*(nums[1]**2)) + 6*((nums[0])**5)*(nums[1]) + ((nums[0])**6)
print(round(p1,3))