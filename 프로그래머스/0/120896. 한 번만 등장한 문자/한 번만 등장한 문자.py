def solution(s):
    answer = ''

    for c in s:
        if s.count(c) == 1:
            answer += c
        else:
            continue
        answer = ''.join(sorted(answer))
    return answer