import heapq

N, K = list(map(int, input().split()))
P = list(map(int, input().split()))


que = P[0:K]
print(min(que))
heapq.heapify(que)
for i in range(K, N):
    p_i = P[i]
    min_que = que[0]
    if(min_que < p_i):
        heapq.heappop(que)
        heapq.heappush(que, p_i)
    print(que[0])
