from collections import deque
import time

N, D = list(map(int, input().split()))
W = []
times = []
times.append(time.time())
for i in range(N):
    l_i, r_i = list(map(int, input().split()))
    W.append([l_i, r_i])
times.append(time.time())


sorted_w = sorted(W, key=lambda x: x[1])
d = deque(sorted_w)

times.append(time.time())
min_r = d.popleft()[1]
answer = 1
while True:
    if(len(d) == 0):
        break
    l, r = d.popleft()
    if(l >= min_r + D):
        answer += 1
        min_r = r
times.append(time.time())
# print(",".join([str(times[i+1] - times[i]) for i in range(len(times) - 1)]))
print(answer)
