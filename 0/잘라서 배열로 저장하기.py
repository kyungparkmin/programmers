def solution(my_str, n):
    return [my_str[i:i+n] for i in range(0, len(my_str), n)]

print(solution('abc1Addfggg4556b', 6))