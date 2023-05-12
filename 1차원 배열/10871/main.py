N, X = input().split()
N = int(N)
X = int(X)

A = input().split()

for idx in range(N):
    num = int(A[idx])
    if X > num:
        print(num, end=" ")