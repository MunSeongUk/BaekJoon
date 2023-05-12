N = int(input())
score = list(map(int, input().split()))

maxScore = max(score)

sum = 0

for idx in range(N):
    score[idx] = (score[idx] / maxScore) * 100
    sum += score[idx]

print(sum / N)