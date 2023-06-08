A, B = input().split()
rA = ""
rB = ""

for idx in range(2, -1, -1):
    rA += A[idx]
    rB += B[idx]

A = int(rA)
B = int(rB)

if A > B:
    print(A)
else:
    print(B)