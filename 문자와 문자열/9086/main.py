T = int(input())

for i in range(T):
    string = input()
    if len(string) > 1:
        print(string[0] + "" + string[len(string) - 1])
    else:
        print(string[0] + "" + string[0])