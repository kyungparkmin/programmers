def solution(num_list):
    answer = [0, 0]
    for i in num_list:
        if num_list[i] % 2 == 0:
            answer[0] += 1
        else:
            answer[1] += 1
    return answer

num_list = [1, 2, 3, 4, 5]

solution(num_list)


""" def solution(num_list):
    answer = [0,0]
    for n in num_list:
        answer[n%2]+=1
    return answer """