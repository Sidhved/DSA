t = int(input())
B = []
for i in range(t):
    bud = int(input())
    B.append(bud)
B.sort()
b = 0
for i in range(t):
    if B[i]*(t-i) >= b:
        b = B[i]*(t-i)
print(b)