def solution(score):
    answer = []
    M = []
    
    for s in score:
        M.append((s[0] + s[1]) / 2)

    for avg in M:
        rank = 1
        
        for other in M:
            if other > avg:
                rank += 1
        
        answer.append(rank)
        
    return answer