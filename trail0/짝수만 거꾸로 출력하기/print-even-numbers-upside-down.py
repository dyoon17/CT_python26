N = int(input())
str = list(map(int, input().split()))

for i in range(N-1, -1, -1):
    if str[i] % 2 == 0:
        print(str[i], end=' ')