A = input()
fruits = ["apple", "banana", "grape", "blueberry", "orange"]
cnt = 0

for fruit in fruits:
    if fruit[2] == A or fruit[3] == A:
        print(fruit)
        cnt +=1
print(cnt)
