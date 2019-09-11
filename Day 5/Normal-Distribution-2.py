import math
a = input()
nums = []
for i in a.split(' '):
    nums.append(float(i))
mean = nums[0]
std = nums[1]
l1 = float(input())
l2 = float(input())
def prob(mean,std,limit):
    return(0.5*(1+math.erf((limit-mean)/(std*(2**0.5)))))
prob1 = (1-prob(mean,std,l1))*100
prob2 = (1-prob(mean,std,l2))*100
prob3 = prob(mean,std,l2)*100
print(round(prob1,2))
print(round(prob2,2))
print(round(prob3,2))