input1 = input()
input2 = input()
input3 = input()
input4 = input()
input5 = input()


idx1 = 0 
idx2 = 0
idx3 = 0
idx4 = 0
idx5 = 0

for i in range(15):
    if idx1 < len(input1):
        print(input1[idx1], end="")
        idx1 += 1
    if idx2 < len(input2):
        print(input2[idx2], end="")
        idx2 += 1
    if idx3 < len(input3):
        print(input3[idx3], end="")
        idx3 += 1
    if idx4 < len(input4):
        print(input4[idx4], end="")
        idx4 += 1
    if idx5 < len(input5):
        print(input5[idx5], end="")
        idx5 += 1