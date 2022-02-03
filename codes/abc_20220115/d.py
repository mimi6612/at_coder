a, N = list(map(int, input().split()))
if N == 1:
    print(0)
    exit()


def op_1(x):
    return x * a


def op_2(x):
    str_x = str(x)
    return int(str_x[-1] + str_x[:-1])


def can_op2(x):
    return x >= 10 and x % 10 != 0


def apply_op_1(hash, key):
    hash[key + "1"] = op_1(hash[key])


num = 1
answer = -1


kouhos = {"": 1}
op1 = 0
op2 = 0

while True:
    new_kouhos = {}
    for key in kouhos:

        value = kouhos[key]
        new_key = key + "1"
        new_value = op_1(kouhos[key])
        new_kouhos[key + "1"] = new_value
        if new_value == N:
            print(len(new_key))

        new_key = key
        new_value = value
        while True:
            if not can_op2(new_value):
                break
            else:
                new_value = op_2(new_value)
                new_key += "2"
                new_kouhos[new_key] = new_value
                if new_value == N:
                    print(len(new_key))
                    exit()
                elif new_value == value:
                    break
    if all([new_kouhos[k] > N for k in new_kouhos]):
        break
    else:
        kouhos = new_kouhos

print(-1)

