def solution(n):
    answer = n
    if n == 1:
       return 4
    
    for i in range(answer):
      if i * i == n:
         break
      
    if i * i != n:
       return -1

    return (i+2) * i+1

print(solution(121))