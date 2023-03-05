def solution(s):
    list = []

    for i in s:
      list.append(i)

    list.sort(reverse=True)

    return ''.join(list)

print(solution("Zbcdefg"))