class CompatibleArray:
    def __init__(self, a):
        self.value = a

    def fetch(self, i, j):
        if i < j:
            return self.value[i][j - i - 1]
        else:
            return self.value[j][i - j - 1]


def calc(n, aishou, selected=[], remain=[]):
    if len(remain) == 0:
        remain = list(range(2 * n))
    answer = 0
    d1 = remain.pop(0)
    selected.append(d1)
    for idx in range(len(remain)):
        d2 = remain.pop(idx)
        selected.append(d2)
        if len(selected) == 2 * n:
            sum_aishou = 0
            for i in range(n):
                sum_aishou ^= aishou.fetch(selected[2 * i], selected[2 * i + 1])

            if answer < sum_aishou:
                answer = sum_aishou
        else:
            sum_aishou = calc(n, aishou, selected, remain)
            if answer < sum_aishou:
                answer = sum_aishou
        remain.insert(idx, d2)
        selected.pop()
    remain.insert(0, d1)
    selected.pop()
    return answer


N = int(input())
A = []
for i in range(2 * N - 1):
    A.append(list(map(int, input().split())))

AISHOU = CompatibleArray(A)

print(calc(N, AISHOU))

