def solution(my_string, n):
    answer = []
    for i in my_string:
        for _ in range(n):
            answer.append(i)
    answer = ''.join(answer)
    print(answer)
    return answer

solution('hello', 3)