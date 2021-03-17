for i in range(int(input())):
    K, D0, D1 = map(int, input().split())
    D = D0 + D1
    if K == 2:
        w = D
    elif K == 3:
        w = D + (D % 10)
    else:
        cycle = ((2 * D) % 10) + ((4 * D) % 10) + ((8 * D) % 10) + ((6 * D) % 10)
        w = D + (D % 10) + (cycle * ((K - 3) // 4)) 
        for X, Y in zip(range((K - 3) % 4), [2, 4, 8, 6]):
            w = w+ (Y * D) % 10
    
    if w%3==0:
        print('YES')
    else:
        print('NO')