def solution(numbers):
    num = ["zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
    
    for i in range(len(num)):
        numbers = numbers.replace(num[i], str(i))
    return int(numbers)