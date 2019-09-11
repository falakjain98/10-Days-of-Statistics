import math
a = float(input())
b = int(input())
prob = (math.exp(-a)*(a**b))/math.factorial(b)
print(round(prob,3))