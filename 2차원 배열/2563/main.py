N = int(input())

square = [[0 for row in range(100)] for col in range(100)]

for i in range(N):
    x, y = map(int, input().split())
    
    for col in range(y, y + 10):
        for row in range(x, x + 10):
            square[col][row] += 1


area = 0

for col in range(0, 100):
    for row in range(0, 100):
        if square[col][row] >= 1:
            area += 1

print(area)