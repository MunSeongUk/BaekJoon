alphabets = [-1] * 26

S = input()
step = 1

for char in S:
    idx = ord(char) - ord('a')
    if alphabets[idx] == -1:
        alphabets[idx] += step
    step += 1

for char in alphabets:
    print(char, end=' ')