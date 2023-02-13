my_string = 'Bacd'

def solution(my_string):
    answer = ''.join(sorted(my_string.lower()))
    return answer

solution(my_string)