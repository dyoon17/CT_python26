def solution(numbers):
    numbers.sort()
    
    for i in range(len(numbers)):
        answer = numbers[i-1] * numbers[i]    
    return answer