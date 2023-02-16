def solution(order):
    answer = 0
    li = list(str(order))
    for i in li:
        if i == 0:
            continue
        if int(i) % 3 == 0:
            answer += 1
    return answer


print(solution(29423))