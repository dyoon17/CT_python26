def solution(hp):
    cnt = 0
    if hp % 5 == 0:
        cnt += hp // 5
    else:
        if (hp % 5) % 3 == 0:
            cnt += hp // 5 + (hp % 5) // 3
        else:
            cnt += hp // 5 + (hp % 5) // 3 + ((hp % 5) % 3) // 1
    
    return cnt