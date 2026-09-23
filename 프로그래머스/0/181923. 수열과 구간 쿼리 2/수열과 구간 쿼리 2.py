def solution(arr, queries):
    answer = []
    
    for query in queries:
        new = []
        for i in range(query[0], query[1]+1):
            if arr[i] > query[2]:                
                new.append(arr[i])                
            else:
                continue
        
        if new == []:
            answer.append(-1)
        else:
            answer.append(min(new))
                
    return answer