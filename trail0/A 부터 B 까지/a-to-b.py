A, B = map(int, input().split())
num = A

while True:
    print(num, end=' ')
    if num % 2 == 1:
        num *= 2
    else:
        num += 3
    if num > B:
        break