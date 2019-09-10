# Enter your code here. Read input from STDIN. Print output to STDOUT
import math
a = input()
nums = []
for i in a.split(' '):
    nums.append(int(i))
nums[0] = nums[0]/100
p1 = ((math.factorial(nums[1])/(2*math.factorial(nums[1]-2)))*((nums[0])**2)*((1-nums[0])**(nums[1]-2))) + (nums[1])*(nums[0])*((1-nums[0])**(nums[1]-1)) + ((1-nums[0])**(nums[1]))
p2 = 1-p1+((math.factorial(nums[1])/(2*math.factorial(nums[1]-2)))*((nums[0])**2)*((1-nums[0])**(nums[1]-2)))
print(round(p1,3))
print(round(p2,3))