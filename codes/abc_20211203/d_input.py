from random import randint
N = 2 * 10**5
print(f"{N} 1")
for i in range(N):
    l_i = randint(1, 10**9)
    r_i = randint(l_i, 10**9)
    print(f"{l_i} {r_i}")
