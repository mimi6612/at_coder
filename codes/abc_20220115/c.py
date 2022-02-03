N, Q = list(map(int, input().split()))
a = list(map(int, input().split()))

queries = {}
freq = {}

for i in range(N):
    idx = i + 1
    a_i = a[i]

    if a_i in freq:
        freq[a_i] += 1
    else:
        freq[a_i] = 1

    key = f"{a_i}_{freq[a_i]}"
    queries[key] = idx


for i in range(Q):
    x_i, k_i = list(map(int, input().split()))
    key = f"{x_i}_{k_i}"
    if key in queries:
        print(queries[key])
    else:
        print("-1")

