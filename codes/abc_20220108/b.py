import math
N = int(input())
points = []
for i in range(N):
    x_i, y_i = list(map(int, input().split()))
    points.append([x_i, y_i])

answer = 0
for i in range(N):
    for j in range(N):
        x_i, y_i = points[i]
        x_j, y_j = points[j]
        dist = math.sqrt((y_j - y_i)**2 + (x_j - x_i)**2)

        if answer < dist:
            answer = dist
print(answer)
