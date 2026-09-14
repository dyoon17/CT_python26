def solution(babbling):
    answer = 0
    W = ["aya", "ye", "woo", "ma"]
    
    for b in babbling:
        for word in W:
            b = b.replace(word, ' ')
                
        if b.strip() == '':
            answer += 1
                    
    return answer