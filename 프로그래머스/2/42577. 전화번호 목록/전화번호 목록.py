def solution(phone_book):
    answer = True
    
    new = sorted(phone_book)
    
    for i in range(0, len(new)-1):
        if new[i] == new[i+1][:len(new[i])]:
            answer = False
        else:
            continue
    
    return answer