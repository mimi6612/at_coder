L, R = list(map(int, input().split()))
S = input()

sub_s1 = S[0:L-1]
sub_s2 = S[L-1:R]
sub_s3 = S[R:]

result = sub_s1 + sub_s2[::-1] + sub_s3
print(result)
