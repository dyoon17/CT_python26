def solution(numbers, direction):
    if direction == "left":
        x = numbers.pop(0)
        numbers.append(x)
    else:
        x = numbers.pop()
        numbers.insert(0, x)
    return numbers