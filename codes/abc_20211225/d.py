def get_array_sum(array):
    array_sum = [0] * len(array)
    array_sum[0] = array[0]
    for i in range(len(array) - 1):
        array_sum[i+1] = array_sum[i] + array[i+1]
    return array_sum


N, K = list(map(int, input().split()))
input_a = list(map(int, input().split()))
array_sum = get_array_sum(input_a)

sum_count_hash = {}
sum_count_hash[0] = 1
answer = 0
for r in range(N):
    if(sum_count_hash.get(array_sum[r] - K)):
        answer += sum_count_hash[array_sum[r] - K]

    if not sum_count_hash.get(array_sum[r]):
        sum_count_hash[array_sum[r]] = 1
    else:
        sum_count_hash[array_sum[r]] += 1

print(answer)
