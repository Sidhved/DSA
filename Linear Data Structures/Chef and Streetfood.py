for i in range(int(input())):
    n = int(input())
    profit = 0
    for j in range(n):
        (s, p, v) = map(int, input().split())
        profit = max(profit, (p//(s+1)*v))
    print(profit)