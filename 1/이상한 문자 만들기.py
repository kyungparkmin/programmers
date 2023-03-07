def solution(s):

    li = s.split(' ')
    word = []
    answer = []
    for i in li:
        word.append(list(i))

    for i in word:
        for j in range(len(i)):
            if j % 2 == 0:
                answer.append(i[j].upper())
            else:
                answer.append(i[j].lower())
        answer.append(' ')
    
    return ''.join(answer)[:-1]


print(solution('try hello world'))