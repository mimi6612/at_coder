import math

X, Y = list(map(int, input().split()))

if Y < X:
    n = 0
else:
    n = math.ceil((Y - X) / 10)

print(n)
