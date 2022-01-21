import math
N = int(input())

answer = 0
a = 1
floor_root_n = math.floor(math.sqrt(N))
i = N
while True:
    end = math.floor(N / a)
    start = math.floor(N / (a + 1)) + 1
    i -= (end - start + 1)
    if i > floor_root_n:
        answer += (end - start + 1) * a
    else:
        start = floor_root_n + 1
        answer += (end - start + 1) * a
        break
    a += 1
for i in range(1, floor_root_n + 1):
    answer += math.floor(N / i)
print(answer)
