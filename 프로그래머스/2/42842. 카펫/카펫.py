def solution(brown, yellow):
    answer = []
    y = []
    total = []
    
    for i in range(1, yellow + 1):
        if yellow % i == 0:
            y.append(i)
            
    for i in range(1, brown + yellow + 1):
        if (brown + yellow) % i == 0:
            total.append(i)
            
    for w in total:
        h = (brown + yellow) // w
        if (h - 2) * (w - 2) == yellow:
            if w >= h:
                answer.append(w)
                answer.append(h)
            
    return answer