
class NumberDigit:
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return ''.join([str(v) for v in self.value])

# n桁で 0,2 のみからなる正整数の数を返す


def calc_number_of_integer(n):
    return 2**(n-1)

# n桁の0,2 のみからなる正整数のうちに小さいものからk番目の数字をNumberDigitの形で返す


def calc_integer(n, k):
    sum = 0
    array = []
    for i in range(1, n+1):
        if i == 1:
            array.append(2)
        else:
            diff = 2**(n-i)
            if(k <= sum + diff):
                array.append(0)
            else:
                sum += diff
                array.append(2)
    return NumberDigit(array)


K = int(input())

ndigit = 0
pre_sum = 0
sum = 0
while sum < K:
    pre_sum = sum
    ndigit += 1
    sum += calc_number_of_integer(ndigit)


number_digit = calc_integer(ndigit, K - pre_sum)
print(str(number_digit))
