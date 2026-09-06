def solution(s):
    numbers = []
    for i in s.split():
        if i != "Z":
            numbers.append(int(i))
        else:
            numbers.pop()
    answer = sum(numbers)
    return answer