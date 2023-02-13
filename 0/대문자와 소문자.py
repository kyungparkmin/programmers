def solution(my_string):
    str_list = []
    for i in my_string:
        if i.isupper() == True:
            str_list.append(i.lower())
        else:
            str_list.append(i.upper())

    return ''.join(i for i in str_list)



print(solution('cccCCC'))
