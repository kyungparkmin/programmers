def solution(s):
    list = []
    for i in s.split(' '):
        try:
            list.append(int(i))
        except:
            if list:
                list.pop()
    return sum(list)

print(solution('1 2 Z 3'))