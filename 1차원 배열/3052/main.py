listOfRemainder = [0] * 42

for _ in range(10):
    n = int(input())
    idx = n % 42
    listOfRemainder[idx] += 1

answer = 0
for idx in range(42):
    if listOfRemainder[idx] >= 1:
        answer += 1

print(answer) 