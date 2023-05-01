N = int(input())

numOfLong = N // 4

if N % 4:
    numOfLong += 1

for idx in range(numOfLong):
    print("long", end=" ")

print("int")