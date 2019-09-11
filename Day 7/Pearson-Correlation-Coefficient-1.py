import statistics

n = int(input())
X = input()
Y = input()

X, Y = X.split(' '), Y.split( ' ')
X.pop()
X = [float(x) for x in X]
Y = [float(y) for y in Y]
meanx = statistics.mean(X)
stdx = statistics.pstdev(X)
meany = statistics.mean(Y)
stdy = statistics.pstdev(Y)
sums = 0
for i in range(len(X)):
    sums = sums + ((X[i]-meanx)*(Y[i]-meany))
print(round(sums/(len(X)*stdx*stdy),3))