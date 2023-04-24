X = int(input())
N = int(input())

stage = 0
sum = 0

while stage < N:
    a, b = input().split()
    a = int(a)
    b = int(b)

    sum += a * b
    stage += 1

if sum == X:
    print("Yes")
else:
    print("No")
