def solution(x):
    num_list = list(map(int, str(x)))
    su = sum(num_list)

    return x % su == 0


print(solution(10))