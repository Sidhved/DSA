for _ in range(int(input())):
    n, k = map(int, input().split())
    A = list(map(int, input().split()))
    l = temp = count = 0
    m = [0]*(k+1)
    for i in range(n):
        m[A[i]] += 1
        if m[A[i]] == 1:
            count += 1
        while count > (k-1):
            m[A[temp]] -= 1
            if m[A[temp]] == 0:
                count -= 1
            temp += 1
        l = max(l, i-temp+1)
    l = max(l, (i-temp+1))
    print(l)