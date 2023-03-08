def solution(s):
  answer = list(map(int, s.split()))

  result = str(min(answer)) + " " + str(max(answer))

  return result
  



print(solution('-1 -2 -3 -4'))