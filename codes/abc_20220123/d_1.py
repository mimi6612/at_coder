# 組み合わせ総数は全組み合わせの半分
# (組み合わせの条件に番号の大小が絡むため)

# 考察1
# 小さい方を先に決めてしまう
# bit全探索で1になる値を小さい方として考える
# 順列全探索
# TLE

import copy
from collections import defaultdict
import sys

sys.setrecursionlimit(10 ** 7)
n = int(input())
A = [list(map(int, input().split())) for _ in range(2 * n - 1)]

ans = 0
used = defaultdict(bool)


def dfs(depth, temp_ans: int):
    global ans
    if depth == n:
        ans = max(ans, temp_ans)
        return

    # 小さい方
    for i in range(1, 2 * n + 1):
        if not used[i]:
            used[i] = True
            break

    # 大きい方
    for j in range(i + 1, 2 * n + 1):
        if not used[j]:
            used[j] = True
            a = A[i - 1][j - i - 1]
            dfs(depth + 1, temp_ans ^ a)
            used[j] = False
    used[i] = False


dfs(0, 0)

print(ans)
