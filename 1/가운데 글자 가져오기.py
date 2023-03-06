from math import floor

def solution(s):
    if len(s) % 2 == 1:
        return s[floor(len(s) / 2)]
    else:
        return s[floor(len(s) / 2 - 1)]+s[floor(len(s) / 2)]

print(solution('abcd'))