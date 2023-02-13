def solution(array, n):
    answer = 0
    for i in array:
        if i == n:
            answer += 1
    return answer

array = [1, 1, 2, 3, 4, 5]

solution(array, 1)

""" def solution(array, n):
    return array.count(n) """