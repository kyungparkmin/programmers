def solution(phone_number):
    answer = ''
    for i in range(len(phone_number)-4):
      answer.replace(phone_number, '*')
    return answer

print(solution('01033334444'))