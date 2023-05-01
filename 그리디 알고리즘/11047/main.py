N, K = input().split()

N = int(N)
K = int(K)

Arr = []

answer = 0

for idx in range(N):
    Arr.append(int(input()))

for idx in range(N - 1, -1, -1):
    if (K == 0): break
    
    quote = K // Arr[idx]
    answer += quote

    K = K - quote * Arr[idx]

print(answer)