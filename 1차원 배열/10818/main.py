N = int(input())

list = input().split()

min = int(list[0])
max = int(list[0])

for idx in range(1, N):
    num = int(list[idx])

    if min > num:
        min = num
    if max < num:
        max = num

print("{} {}".format(min, max))

    