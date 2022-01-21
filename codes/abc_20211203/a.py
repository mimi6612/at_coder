N = int(input())
n = N
if N >= 42:
    n += 1
XXX = str(n).zfill(3)
answer = f'AGC{XXX}'
print(answer)
