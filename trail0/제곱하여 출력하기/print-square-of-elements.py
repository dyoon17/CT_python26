N = int(input())
x = list(map(int, input().split()))

for i in range(N):
    print(x[i] ** 2, end=' ')