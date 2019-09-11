import statistics

n = int(input())
X = input()
Y = input()

X, Y = X.split(' '), Y.split( ' ')
X.pop()
X = [float(x) for x in X]
Y = [float(y) for y in Y]
indexx = [0]*len(X)
for i in range(len(X)):
    indexx[X.index(min(X))] = i+1
    X[X.index(min(X))] = max(X)+1
indexy = [0]*len(Y)
for i in range(len(Y)):
    indexy[Y.index(min(Y))] = i+1
    Y[Y.index(min(Y))] = max(Y)+1
d=0
for i in range(n):
    d = d + (indexx[i]-indexy[i])**2
print(round(1-((6*d)/(n*(n**2-1))),3))