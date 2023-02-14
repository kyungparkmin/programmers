def solution(cipher, code):
    answer = ''
    n = 0
    for i in cipher:
        n += 1
        if  n % code == 0:
            answer = answer + i
    return answer

print(solution('dfjardstddetckdaccccdegk', 4))