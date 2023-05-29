listOfStudentNo = [0] * 31

for idx in range(28):
    studentNo = int(input())
    listOfStudentNo[studentNo] = 1

for idx in range(1, 31):
    if listOfStudentNo[idx] == 0:
        print(idx)