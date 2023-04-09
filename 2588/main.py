A = int(input())
B = int(input())
S = 0
cnt = 0

while B > 0:
    C = B % 10
    if cnt != 0:
        S += A * C * (10 ** cnt)
    else:
        S += A * C
    print(A * C)
    B = B // 10
    cnt = cnt + 1

print(S)