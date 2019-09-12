import math
import statistics
m1 = []
m2 = []
for i in range(5):
    a = input()
    a = a.split(' ')
    m1.append(int(a[0]))
    m2.append(int(a[1]))
sumx=sum(m1)
sumy=sum(m2)
sumxy=0
for i in range(5):
    sumxy = sumxy + m1[i]*m2[i]
sumx2=0
for i in range(5):
    sumx2 = sumx2 + m1[i]**2
b = (5*sumxy - sumx*sumy)/(5*sumx2 - sumx**2)
xmean = sum(m1)/5
ymean = sum(m2)/5
a = ymean - b*xmean
print(round(a+b*80,3))