import math
a = input()
nums = []
for i in a.split(' '):
    nums.append(float(i))
mean = nums[0]
std = nums[1]
l = float(input())
b = input()
nums=[]
for i in b.split(' '):
    nums.append(float(i))
l1 = nums[0]
l2 = nums[1]
def prob(mean,std,limit):
    return(0.5*(1+math.erf((limit-mean)/(std*(2**0.5)))))
prob1 = prob(mean,std,l)
prob2 = prob(mean,std,l2) - prob(mean,std,l1)
print(round(prob1,3))
print(round(prob2,3))