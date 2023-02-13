def solution(numbers):
    for i in range(len(numbers)):
        numbers[i] *= 2
    return numbers

numbers = [1, 2, 3, 4, 5]

solution(numbers)