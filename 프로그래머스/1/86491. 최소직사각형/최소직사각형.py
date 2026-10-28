def solution(sizes):
    answer = 0
    new = []
    l = 0
    w = 0
    
    for i in range(len(sizes)):
        sizes[i] = sorted(sizes[i])
        new.append(sizes[i])
    
    for i in range(len(new)):
        for j in range(len(new)):
            if new[i][0] > l:
                l = new[i][0]
            if new[i][1] > w:
                w = new[i][1]
                
    answer = l * w
    return answer