def solution(array):
    answer = 0
    for i in array:
        for c in str(i):
            if c == '7':
                answer += 1
    return answer