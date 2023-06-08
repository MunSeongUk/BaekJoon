T = int(input())

idx = 0
answers = []

while idx < T:
    R, S = input().split(" ")
    R = int(R)

    for char in S:
        tmp = ""
        tmp += char * R
        answers.append(tmp)
    idx += 1

for answer in answers:
    print(answer)