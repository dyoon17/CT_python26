def solution(rank, attendance):
    answer = 0
    new = []
    
    for i in range(len(rank)):
        if attendance[i] == True:
            new.append(rank[i])
        
    new.sort()
    
    for i in range(len(rank)):
        if rank[i] == new[0]:
            answer += 10000 * i
        elif rank[i] == new[1]:
            answer += 100 * i
        elif rank[i] == new[2]:
            answer += i
    
    return answer