def solution(my_string, letter):
    answer = []
    for i in my_string:
        if i == letter:
            continue
        else:
            answer.append(i)
    answer = ''.join(answer)
    return answer

solution('abcdef', 'f')



""" def solution(my_string, letter):
    return my_string.replace(letter, '') """