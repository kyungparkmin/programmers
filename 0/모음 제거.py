def solution(my_string):
    answer = ''
    for i in my_string:
        if i == 'a' or i == 'e' or i == 'i' or i == 'o' or i == 'u':
            continue
        else:
            answer += i
    return answer

""" def solution(my_string):
    vowels = ['a','e','i','o','u']
    for vowel in vowels:
        my_string = my_string.replace(vowel, '')
    return my_string """