def solution(before, after):
    answer = 0
    before.split()
    before = sorted(before)
    after.split()
    after = sorted(after)
    
    if before == after:
        answer = 1
    return answer