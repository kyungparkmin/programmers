def solution(n):
    temp = n ** 0.5
    if int(temp) == temp:
      if temp ** 2 == n:
        return 1
    return 2