def solution(my_string, letter):
    answer = ''
    for c in my_string:
        if c == letter:
            continue
        else:
            answer += c
    return answer