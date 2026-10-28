def solution(array, commands):
    answer = []
    new = []
    
    for com in commands:
        new = array[com[0]-1:com[1]]
        new = sorted(new)
        answer.append(new[com[2]-1])
    
    return answer