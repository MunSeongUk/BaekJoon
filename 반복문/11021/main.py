import sys

T = int(sys.stdin.readline())

for idx in range(T):
    A, B = map(int, sys.stdin.readline().split())
    print("Case #{}: {}".format(idx + 1, A + B))