t = int(input())
for i in range(t):
    n = int(input())
    S = list(map(int, input().split()))
    c = 0
    while S:
        m = min(S)
        p = S.index(m)
        c = c + (len(S) - p)*m
        S = S[0:p]
    print(c)