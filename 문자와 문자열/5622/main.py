alphabets = [3, 3, 3, 4, 4, 4, 5, 5, 5, 6, 6, 6, 7, 7, 7, 8, 8, 8, 8, 9, 9, 9, 10, 10, 10, 10]

S = input()

answer = 0

for char in S:
    answer += alphabets[ord(char) - ord('A')]

print(answer)
