N, Y = map(int, input().split())

def search_otoshidama(n, y):
    max_n3 = y / 1000
    kouho = [0, 0, max_n3]
    if max_n3 < n:
        return [-1, -1, -1]

    max_n1 = y // 10000
    for n1 in range(max_n1 + 1):
        max_n2 = (y - 10000 * n1) // 5000
        for n2 in range(max_n2 + 1):
            n3 = (y - 10000 * n1 - 5000 * n2) // 1000
            kouho = [n1 , n2, n3]
                
            if n1 + n2 + n3 == N:
                return [n1, n2, n3]
    return [-1, -1, -1]

n1, n2, n3 = search_otoshidama(N, Y)
print(n1, n2, n3)


