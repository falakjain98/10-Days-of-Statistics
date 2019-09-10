# Enter your code here. Read input from STDIN. Print output to STDOUT
n = int(input())
a = input()
b = input()
nums=[]
nums1=[]
nums2=[]
for i in a.split(' '):
    nums1.append(int(i))
for i in b.split(' '):
    nums2.append(int(i))
for i in range(n):
    for j in range(int(nums2[i])):
        nums.append(int(nums1[i]))
n=sum(nums2)
nums=sorted(nums)
mid = int(n/4)
if n%2 != 0:
    if ((n-1)/2)%2 != 0:
        q1 = nums[mid]
    else:
        q1 = ((nums[mid]+nums[mid-1])/2)
elif n%4 == 0:
    q1 = ((nums[mid]+nums[mid-1])/2)
else:
    q1 = (nums[mid])
mid = int(3*n/4)
if n%2 != 0:
    if ((n-1)/2)%2 != 0:
        q3 = nums[mid] 
    else:
        q3 = ((nums[mid]+nums[mid+1])/2)
elif n%4 == 0:
    q3 = ((nums[mid]+nums[mid-1])/2)
else:
    q3 = (nums[mid])
print(float(q3-q1))