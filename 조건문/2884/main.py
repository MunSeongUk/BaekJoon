H, M = input().split()

H = int(H)
M = int(M)

if M - 45 < 0:
    H = H - 1
    M = 60 + (M - 45)
else:
    M = M - 45

if H == -1:
    H = 23

print(str(H) + " " + str(M))