t = int(input())

for i in range(t):
    n = int(input())
    for j in range(n):
        (i, n, q) = map(int, input().split())
        pr = int(n/2)
        if i == q:
            print(pr)
        else:
            print(n-pr)