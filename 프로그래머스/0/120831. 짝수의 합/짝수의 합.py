def solution(n):
    sum = 0
    for i in range(1, n+1):
        if  i % 2 == 1:
            continue
        else:
            sum += i
    return sum