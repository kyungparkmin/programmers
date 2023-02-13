def solution(array):
    answer = 0
    array.sort()
    key = int(len(array) / 2)
    answer = array[key]
    return answer

array = [9, -1, 0]
solution(array)