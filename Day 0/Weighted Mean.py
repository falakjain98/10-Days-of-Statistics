# Enter your code here. Read input from STDIN. Print output to STDOUT
n = int(input())
a = input()
w = input()
nums = []
wts =[]
sums=0
for i in a.split(' '):
    nums.append(int(i))
for i in w.split(' '):
    wts.append(int(i))
for i in range(n):
    sums = sums+(nums[i]*wts[i])
print(round(sums/sum(wts),1))