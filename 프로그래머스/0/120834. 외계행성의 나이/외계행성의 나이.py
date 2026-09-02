def solution(age):
    N = 'abcdefghij'
    answer = ''
    for i in str(age):
        answer += N[int(i)]
    return answer