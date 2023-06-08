T = int(input())

idx = 0
answers = []

while idx < T:
    R, S = input().split(" ")
    R = int(R)
    tmp = ""
    for char in S:
        tmp += char * R
    idx += 1
    answers.append(tmp)

for answer in answers:
    print(answer)