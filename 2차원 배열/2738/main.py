N, M = map(int, input().split())

A = [[0 for i  in range(M + 1)] for i in range(N + 1)]

for i in range(1, N + 1):
    values = list(map(int, input().split()))
    for j in range(1, M + 1):
        A[i][j] = values[j - 1]

for i in range(1, N + 1):
    values = list(map(int, input().split()))
    for j in range(1, M + 1):
        A[i][j] += values[j - 1]

for i in range(1, N + 1):
    for j in range(1, M + 1):
        print(A[i][j], end=" ")
    print()