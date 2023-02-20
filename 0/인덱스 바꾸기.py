def solution(my_string, num1, num2):
    answer = ''
    answer = my_string.replace(my_string[1], my_string[2])
    print()
    print(answer.replace(my_string[2], my_string[1]))
    return answer

print(solution('hello', 1, 2))