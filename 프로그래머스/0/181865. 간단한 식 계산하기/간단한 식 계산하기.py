def solution(binomial):
    answer = 0
    new = binomial.split()
    
    if new[1] == '+':
        answer = int(new[0]) + int(new[2])
    elif new[1] == '-':
        answer = int(new[0]) - int(new[2])
    elif new[1] == '*':
        answer = int(new[0]) * int(new[2])
    return answer