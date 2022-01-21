class BoxChecker:
    def __init__(self, n, a, b):
        self.n = n
        self.a = a
        self.b = b
        self.min_k1 = max(1 - self.a, 1 - self.b)
        self.max_k1 = min(self.n - a, self.n - b)
        self.min_k2 = max(1-self.a, self.b - self.n)
        self.max_k2 = min(self.n - self.a, self.b - 1)

    def check_point(self, x, y):
        if x - self.a == y - self.b:
            k = x - self.a
            if(self.min_k1 <= k and k <= self.max_k1):
                return '#'
            else:
                return '.'
        elif x - self.a == -(y - self.b):
            k = x - self.a
            if(self.min_k2 <= k and k <= self.max_k2):
                return '#'
            else:
                return '.'
        else:
            return '.'

    def check_area(self, p, q, r, s):
        result = ""
        for i in range(p, q + 1):
            s_i = ""
            for j in range(r, s + 1):
                s_i += self.check_point(i, j)
            s_i += "\n"
            result += s_i
        return result


N, A, B = list(map(int, input().split()))
P, Q, R, S = list(map(int, input().split()))
box_checker = BoxChecker(N, A, B)
answer = box_checker.check_area(P, Q, R, S)
print(answer)
