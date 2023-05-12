max = int(input())
maxIdx = 1

for idx in range(2, 10):
    tmp = int(input())

    if max < tmp:
        max = tmp
        maxIdx = idx

print("{} {}".format(max, maxIdx))