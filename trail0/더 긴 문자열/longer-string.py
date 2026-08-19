N = input().split()

if len(N[0]) > len(N[1]):
    print (N[0], len(N[0]), end=' ')
elif len(N[0]) < len(N[1]):
    print (N[1], len(N[1]), end=' ')
else:
    print("same")
