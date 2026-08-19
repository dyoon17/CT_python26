x = list(map(int, input().split()))

for i in range(8):
    x.append((x[i] + x[i+1]) % 10)

for i in range(10):   
    print(x[i], end=' ')