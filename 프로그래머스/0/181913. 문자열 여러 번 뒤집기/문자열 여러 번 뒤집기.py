def solution(my_string, queries):
    answer = ''
    
    for query in queries:
        middle = my_string[query[0]:query[1]+1]
        middle = middle[::-1]
        answer = my_string[:query[0]] + middle + my_string[query[1]+1:]
        my_string = answer
    return answer