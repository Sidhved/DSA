t = int(input())

for i in range(t):
    n = int(input())
    l = list(map(int, input().split()))
    Max = 1
    a = l[0]
    for j in range(1, n):
        if a>l[j]:
            Max = Max+1
        else:
            l[j] = a
        a = l[j]
    print(Max)