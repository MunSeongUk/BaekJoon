N = int(input())
list = input().split()
V = int(input())

answer = 0

for idx in range(N):
    if V == int(list[idx]):
        answer += 1

print(answer)