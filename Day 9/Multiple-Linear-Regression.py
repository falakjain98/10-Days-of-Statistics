a = input()
m = int(a.split(' ')[0])
n = int(a.split(' ')[1])
X = []
Y = []
for i in range(n):
    a = input()
    a = a.split(' ')
    a = [float(b) for b in a]
    X.append(a[0:m])
    Y.append(a[m])
q = int(input())
Xnew=[]
for i in range(q):
    a = input()
    a = a.split(' ')
    a = [float(b) for b in a]
    Xnew.append(a)

from sklearn import linear_model
lm = linear_model.LinearRegression()
lm.fit(X,Y)
a = lm.intercept_
b = lm.coef_

Ynew = lm.predict(Xnew)
for i in Ynew:
    print(round(i,2))