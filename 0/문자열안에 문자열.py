def solution(str1, str2):
  if str1.find(str2) == -1:
    return 2
  else:
    return 1

print(solution("ppprrrogrammers", "pppp"))


""" def solution(str1, str2):
    answer = 0
    if str2 in str1:
        return 1
    else:
        return 2
    return answer """