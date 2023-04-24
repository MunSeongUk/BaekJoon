A, B, C = input().split()

A = int(A)
B = int(B)
C = int(C)

reward = 0

if A == B == C:
    reward = 10000 + (A * 1000)
elif A == B != C:
    reward = 1000 + (A * 100)
elif A != B == C:
    reward = 1000 + (B * 100)
elif A == C != B:
    reward = 1000 + (C * 100)
else:
    big = max(A, B)
    big = max(big, C)
    reward = 100 * big     

print(reward)