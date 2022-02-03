S = input()
a, b = list(map(int, input().split()))

answer = list(S)
answer[a - 1] = S[b - 1]
answer[b - 1] = S[a - 1]
answer = "".join(answer)

print(answer)
