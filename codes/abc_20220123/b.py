N = int(input())
A = list(map(int, input().split()))

freq = {}
for a_i in A:
    if not a_i in freq:
        freq[a_i] = 1
    else:
        freq[a_i] += 1

answer = -1
for num in freq:
    if freq[num] < 4:
        answer = num
        break
print(answer)
