A, B = input().split()
C = input()

A = int(A)
B = int(B)
C = int(C)

H_C = C // 60
M_C = C % 60

A = A + H_C
B = B + M_C

if B >= 60:
    A = A + 1
    B = B - 60

if A >= 24:
    A = A - 24

print(str(A) + " " + str(B))
