def f(x):
    return x**2 + 2*x + 3


t = int(input())
answer = f(f(f(t) + t) + f(f(t)))
print(answer)
