N, X = list(map(int, input().split()))

array_l = []
array_a = []

for i in range(N):
    input_i = list(map(int, input().split()))
    array_l.append(input_i[0])
    array_a.append(input_i[1:])


kouho = []
for i in range(N):
    if i == 0:
        kouho = array_a[0]
    else:
        n = len(kouho)
        new_kouho = []
        for k in kouho:
            for a_i_j in array_a[i]:
                new_kouho.append(k * a_i_j)
        kouho = new_kouho
kekka = len(list(filter(lambda x: x == X, kouho)))
print(kekka)
