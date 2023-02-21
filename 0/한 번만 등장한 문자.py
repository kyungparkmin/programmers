def solution(s):
    answer = ''
    s = list(s)
    s.sort()
    s_count = {}
    s_list = []

    for i in s:
        try:
            s_count[i] += 1
        except:
            s_count[i] = 1

    for k, v in s_count.items():
        if v == 1:
            s_list.append(k)
    
    return answer.join(s_list)

print(solution('abdc'))