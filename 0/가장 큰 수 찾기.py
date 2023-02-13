def solution(array):
    answer = []
    max = 0
    key = 0
    for i in range(len(array)):
        if(array[i] > max):
            max = array[i]
            key = i
    answer.append(max)
    answer.append(key)
    return answer

array = [1, 8, 3]

solution(array)




""" def solution(array):
    answer = []
    answer.append(max(array))
    answer.append(array.index(max(array)))
    return answer """

""" def solution(array):
    return [max(array), array.index(max(array))] """