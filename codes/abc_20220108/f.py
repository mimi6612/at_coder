import math
import string
import time


def string_to_hash(str):
    hash = {}
    for s in str:
        if s not in hash:
            hash[s] = 1
        else:
            hash[s] += 1
    return hash


def calc_combination(hash):
    n = 0
    div = 1
    for key in hash:
        n += hash[key]
        if hash[key] > 0:
            div *= math.factorial(hash[key])

    if n == 0:
        return 0
    else:
        return math.factorial(n) // div


def list_hash(hash, idx=0, prev_hash={}):
    abc_list = string.ascii_lowercase
    if idx == len(abc_list):
        return [prev_hash]
    else:
        alphabet = abc_list[idx]
        array = []
        if alphabet in hash:
            for i in range(0, hash[alphabet] + 1):
                new_prev_hash = prev_hash.copy()
                new_prev_hash[alphabet] = i
                array += list_hash(hash, idx + 1, new_prev_hash)

        else:
            array += list_hash(hash, idx+1, prev_hash)

        return array


def calc(s):
    kekka = 0
    length = len(s)
    times = []
    times.append(time.time())
    hash_s = string_to_hash(s)
    times.append(time.time())
    all_hash = list_hash(hash_s)
    times.append(time.time())
    for hash in all_hash:
        c = calc_combination(hash)
        kekka += c
        if kekka > 998244353:
            kekka -= 998244353
    times.append(time.time())
    print([times[i+1] - times[i] for i in range(len(times) - 1)])

    return kekka


def calc_c(j, k, factorial_hash):
    if k == 0 or k == j:
        return 1
    else:
        if not j in factorial_hash:
            factorial_hash[j] = math.factorial(j)
        if not k in factorial_hash:
            factorial_hash[k] = math.factorial(k)
        if not j - k in factorial_hash:
            factorial_hash[j - k] = math.factorial(j - k)
        return factorial_hash[j] // factorial_hash[k] // factorial_hash[j-k]


def calc_2(s):
    abc_list = string.ascii_lowercase
    nalphabet = len(abc_list)
    n = len(s)
    dp = [[0] * (n+1) for i in range(nalphabet)]

    hash_s = string_to_hash(s)

    for j in range(0, n+1):
        if j <= hash_s['a']:
            dp[0][j] = 1
        else:
            break
    for i in range(1, nalphabet):
        char = abc_list[i]
        if not char in hash_s:
            for j in range(0, n+1):
                dp[i][j] = dp[i-1][j]
            continue
        freq_i = hash_s[char]
        dp[i][0] = 1
        factorial_hash = {}
        for j in range(1, n+1):
            for k in range(0, min(j, freq_i) + 1):
                dp[i][j] += calc_c(j, k, factorial_hash) * dp[i - 1][j - k]
            if dp[i][j] == 0:
                break
    return sum(dp[-1][1:]) % 998244353


S = input()
print(calc_2(S))
