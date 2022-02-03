N = int(input())
H = list(map(int, input().split()))

answer = 0
idx = 0
while True:
    if idx == N:
        break

    h = H[idx]
    if answer < h:
        answer = h
    else:
        break
    idx += 1
print(answer)
