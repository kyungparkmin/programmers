from collections import Counter

def solution(array):
    c = Counter(array)
    mode = c.most_common(2)
    print(len(mode))
    if len(mode) <= 2:
      return -1
    else:
      return mode[0][0]



print(solution([1, 2, 3, 3, 3, 4]))