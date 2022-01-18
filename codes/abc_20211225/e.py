X = input()
n = len(X)
answer = 0
for i in range(n):
    answer += int(X)
    X = X[:-1]
print(answer)
