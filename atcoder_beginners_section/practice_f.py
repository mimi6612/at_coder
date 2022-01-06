N, A, B = list(map(int, input().split()))

def get_each_digits(n):
    digits = []
    while(n >= 10):
        digits.append(n % 10)
        n = n // 10
    digits.append(n)
    return digits

num = 0
for i in range(1, N + 1):
    digits = get_each_digits(i)
    sum_each_digits = sum(digits)
    if A <= sum_each_digits and sum_each_digits <= B:
        num += i
print(num)

