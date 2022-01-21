class NumberDigit:
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return ''.join([str(v) for v in self.value])

    def __le__(self, other):
        if not isinstance(other, NumberDigit):
            return NotImplemented
        if self.ndigit() < other.ndigit():
            return True
        elif other.ndigit() < self.ndigit():
            return False
        else:
            for i in range(0, self.ndigit()):
                if self.value[i] < other.value[i]:
                    return True
                elif other.value[i] < self.value[i]:
                    return False
            return True

    def ndigit(self):
        return len(self.value)


# n桁の等差数のリストを返す
# return Array<NumberDigit>


def calc_tousasuu(n):
    array_tousasuu = []
    for i in range(1, 10):
        for d in range(-9, 10):
            value = list(map(lambda x: i + d*x, list(range(0, n))))
            if all(0 <= x and x <= 9 for x in value):
                array_tousasuu.append(NumberDigit(value))
    return array_tousasuu


def min_tousasuu(n):
    if n == 1:
        return NumberDigit([1])
    elif n == 2:
        return NumberDigit([1, 0])
    else:
        return NumberDigit([1] * n)


X = NumberDigit(list(map(int, input())))
ndigit = X.ndigit()
array_tousasuu = calc_tousasuu(ndigit)
for tousasuu in array_tousasuu:
    if X <= tousasuu:
        print(str(tousasuu))
        exit()
print(str(min_tousasuu(ndigit + 1)))
