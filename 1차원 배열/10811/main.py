N, M = map(int, input().split())

basket = list(range(0, N + 1))

for _ in range(M):
    i, j = map(int, input().split())
    count = 0
    for offset in range(((j - i + 1) // 2)):

        tmp = basket[i + offset]
        basket[i + offset] = basket[j - offset]
        basket[j - offset] = tmp

for idx in range(1, N + 1):
    print(basket[idx], end=" ")