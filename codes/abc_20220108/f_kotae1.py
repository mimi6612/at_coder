from heapq import heapify, heappop, heappush


def Primitive_Root(p):
    """Z/pZ上の原始根を見つける

    p:素数
    """
    if p == 2:
        return 1
    if p == 998244353:
        return 3
    if p == 10**9+7:
        return 5
    if p == 163577857:
        return 23
    if p == 167772161:
        return 3
    if p == 469762049:
        return 3

    fac = []
    q = 2
    v = p-1

    while v >= q*q:
        e = 0
        while v % q == 0:
            e += 1
            v //= q

        if e > 0:
            fac.append(q)
        q += 1

    if v > 1:
        fac.append(v)

    g = 2
    while g < p:
        if pow(g, p-1, p) != 1:
            return None

        flag = True
        for q in fac:
            if pow(g, (p-1)//q, p) == 1:
                flag = False
                break

        if flag:
            return g

        g += 1

# 参考元 https://atcoder.jp/contests/practice2/submissions/16789717


def NTT(A):
    """AをMod を法とする数論変換を施す

    ※Modはグローバル変数から指定
    """
    primitive = Primitive_Root(Mod)

    N = len(A)
    H = (N-1).bit_length()

    if Mod == 998_244_353:
        m = 998_244_352
        u = 119
        e = 23
        S = [1, 998244352, 911660635, 372528824, 929031873,
             452798380, 922799308, 781712469, 476477967, 166035806,
             258648936, 584193783, 63912897, 350007156, 666702199,
             968855178, 629671588, 24514907, 996173970, 363395222,
             565042129, 733596141, 267099868, 15311432]
    else:
        m = Mod-1
        e = ((m & -m)-1).bit_length()
        u = m >> e
        S = [pow(primitive, (Mod-1) >> i, Mod) for i in range(e+1)]

    for l in range(H, 0, -1):
        d = 1 << l - 1
        U = [1]*(d+1)
        u = 1
        for i in range(d):
            u = u*S[l] % Mod
            U[i+1] = u

        for i in range(1 << H - l):
            s = 2*i*d
            for j in range(d):
                A[s], A[s+d] = (A[s]+A[s+d]) % Mod, U[j]*(A[s]-A[s+d]) % Mod
                s += 1

# 参考元 https://atcoder.jp/contests/practice2/submissions/16789717


def Inverse_NTT(A):
    """AをMod を法とする逆数論変換を施す

    ※Modはグローバル変数から指定
    """
    primitive = Primitive_Root(Mod)

    N = len(A)
    H = (N-1).bit_length()

    if Mod == 998244353:
        m = 998_244_352
        e = 23
        u = 119
        S = [1, 998244352, 86583718, 509520358, 337190230,
             87557064, 609441965, 135236158, 304459705, 685443576,
             381598368, 335559352, 129292727, 358024708, 814576206,
             708402881, 283043518, 3707709, 121392023, 704923114, 950391366,
             428961804, 382752275, 469870224]
    else:
        m = Mod-1
        e = (m & -m).bit_length()-1
        u = m >> e

        inv_primitive = pow(primitive, Mod-2, Mod)
        S = [pow(inv_primitive, (Mod-1) >> i, Mod) for i in range(e+1)]

    for l in range(1, H + 1):
        d = 1 << l - 1
        for i in range(1 << H - l):
            u = 1
            for j in range(2*i*d, (2*i+1)*d):
                A[j+d] *= u
                A[j], A[j+d] = (A[j] + A[j+d]) % Mod, (A[j] - A[j+d]) % Mod
                u = u * S[l] % Mod

    N_inv = pow(N, Mod-2, Mod)
    for i in range(N):
        A[i] = A[i]*N_inv % Mod

# 参考元 https://atcoder.jp/contests/practice2/submissions/16789717


def Convolution_Mod(A, B):
    """A,BをMod を法とする畳み込みを求める.

    ※Modはグローバル変数から指定
    """
    if not A or not B:
        return []

    N = len(A)
    M = len(B)
    L = N+M-1
    if min(N, M) <= 50:
        if N < M:
            N, M = M, N
            A, B = B, A

        C = [0]*L
        for i in range(N):
            for j in range(M):
                C[i+j] += A[i]*B[j]
                C[i+j] %= Mod

        return C

    H = L.bit_length()
    K = 1 << H

    A = A+[0]*(K-N)
    B = B+[0]*(K-M)

    NTT(A)
    NTT(B)

    for i in range(K):
        A[i] = A[i]*B[i] % Mod

    Inverse_NTT(A)
    return A[:L]

# ==================================================


S = input()
N = len(S)

chi = [0]*26
for a in S:
    chi[ord(a)-ord("a")] += 1

Mod = 998244353
Fact = [1]*(N+1)
Fact_inv = [1]*(N+1)
for i in range(1, N+1):
    Fact[i] = i*Fact[i-1] % Mod
    Fact_inv[i] = pow(Fact[i], Mod-2, Mod)

Q = [(chi[c], Fact_inv[:chi[c]+1]) for c in range(26)]
heapify(Q)

while len(Q) >= 2:
    a, A = heappop(Q)
    b, B = heappop(Q)
    heappush(Q, (a+b, Convolution_Mod(A, B)))

_, A = heappop(Q)
X = 0
for d, a in enumerate(A):
    if d >= 1:
        X += Fact[d]*a
        X %= Mod

print(X)
