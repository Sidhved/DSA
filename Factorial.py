t = int(input())

for i in range(t):
    n = int(input())
    q = 0
    p = 0
    while (n>5**q):
        p = p + n//5**(q+1)
        q = q + 1
    print(p)