N = int(input())
arr = []

for i in range(1, N+1):
    if i % 2 == 0:
        continue
    if i % 3 == 0:
        continue
    if i % 5 == 0:
        continue
    arr.append(i)
print(len(arr))
