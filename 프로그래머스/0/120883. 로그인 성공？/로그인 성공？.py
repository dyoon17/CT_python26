def solution(id_pw, db):
    answer = 'fail'
    
    for arr in db:
        if id_pw[0] == arr[0]:
            if id_pw[1] == arr[1]:
                answer = 'login'
            else:
                answer = 'wrong pw'
            break
                   
    return answer