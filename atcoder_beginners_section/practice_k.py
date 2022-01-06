

def can_travel(from_point, to_point, time):
    move_x = to_point[0] - from_point[0]
    move_y = to_point[1] - from_point[1]
    sum_move = move_x + move_y

    array_sum = []
    for i in range(time + 1):
        array_sum.append(time - 2 * i)
    if(sum_move in array_sum):
        return True
    else:
        return False

N = int(input())
array_t = []
array_point = []
for i in range(N):
    t, x, y = list(map(int, input().split()))
    array_t.append(t)
    array_point.append([x, y])
array_t.insert(0, 0)
array_point.insert(0, [0, 0])

result = True
for i in range(N):
    if not can_travel(array_point[i], array_point[i+1], array_t[i+1] - array_t[i]):
        result = False
if(result):
    print("Yes")
else:
    print("No")



