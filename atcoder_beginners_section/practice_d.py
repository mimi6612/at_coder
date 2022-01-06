N = int(input())
array = list(map(int, input().split()))

def devide(N, array):
    for i in range(N):
        if array[i] % 2 != 0:
            return False
        array[i] = array[i] / 2
    return True

n = 0
while(devide(N, array)):
    n += 1
print(n)

