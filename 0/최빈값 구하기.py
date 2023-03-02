def solution(array):
  count = {}
  for i in array:
    if i not in count:
      count[i] = 1
    else:
      count[i] = count[i]+1

  c1 = sorted(count.values(), reverse=True)

  if len(count) == 1:
    return c1[0]
  
  if c1[0] == c1[1]:
    return -1
  else:
    return c1[0]
    



print(solution([1]))