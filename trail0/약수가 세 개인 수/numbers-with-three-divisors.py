start, end = map(int, input().split())
count = 0
# Please write your code here.
for i in range(start, end+1):
    div = 0
    for j in range(1, i+1):
        if i % j == 0:
            div += 1
    if div == 3:
        count += 1
print(count)