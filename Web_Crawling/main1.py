def solution(s):
    answer = -1
    while 1:
        print(s)
        if len(s) % 2 == 1: return 0
        checker = False
        if len(s) == 0: return 1
        for i in range(1, len(s) - 1):
            if s[i] == s[i-1]:
                s = s[:i] + s[i+1:]
                checker = True
                break
            if i == len(s) - 1 and s[-1] == s[-2]:
                s = s[:-2]
                checker == True
        if checker == False:
            return 0

print(solution("aaccbb"))