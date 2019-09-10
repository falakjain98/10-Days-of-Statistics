# Enter your code here. Read input from STDIN. Print output to STDOUT
n = int(input())
a = input()
nums=[]
for i in a.split(' '):
    nums.append(int(i))
nums=sorted(nums)
mid = int(n/2)
if n%2 != 0:
    q2 = nums[mid]
else:
    q2 = (nums[mid-1]+nums[mid])/2
mid = int(n/4)
if n%2 != 0:
    q1 = int((nums[mid]+nums[mid-1])/2)
else:
    q1 = int(nums[mid])
mid = int(3*n/4)
if n%2 != 0: 
    q3 = int((nums[mid]+nums[mid+1])/2)
elif n%4 == 0:
    q3 = int((nums[mid]+nums[mid-1])/2)
else:
    q3 =  int(nums[mid])
print(q1)
print(int(q2))
print(q3)