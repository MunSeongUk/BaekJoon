A = [[0 for i  in range(9)] for i in range(9)]
maxVal = 0
maxCol = 0
maxRow = 0

for row in range(0, 9):
    values = list(map(int, input().split()))
    for col in range(0, 9):
        if values[col] >= maxVal:
            maxVal = values[col]
            maxCol = col + 1
            maxRow = row + 1

print(maxVal)
print("{} {}".format(maxRow, maxCol))