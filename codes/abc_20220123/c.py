from collections import deque

N, M = list(map(int, input().split()))
S = input().split()
T = deque(input().split())

next_t = T.popleft()
for s in S:
    if s == next_t:
        print("Yes")
        try:
            next_t = T.popleft()
        except IndexError:
            break

    else:
        print("No")
