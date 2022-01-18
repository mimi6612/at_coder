def calc_combination_500_100_50(x):
    combinations = []
    for i in range(x // 500 + 1):
        combinations_100_50 = calc_combination_100_50(x - 500 * i)
        for c in combinations_100_50:
            combinations.append([i] + c)
    return combinations


def calc_combination_100_50(x):
    combinations = []
    for i in range(x // 100 + 1):
        combinations.append([i, (x - 100 * i) // 50])
    return combinations


def valid_combination(combination, A, B, C):
    a, b, c = combination
    if a <= A and b <= B and c <= C:
        return True
    else:
        return False


A = int(input())
B = int(input())
C = int(input())
X = int(input())

all_combinations = calc_combination_500_100_50(X)
valid_combinations = list(
    filter(lambda c: valid_combination(c, A, B, C), all_combinations))

print(len(valid_combinations))
