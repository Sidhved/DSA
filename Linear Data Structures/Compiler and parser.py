T = int(input())
for i in range(T):
    count = 0
    j = 0
    n = input()
    if n[0] == ">":
        print(0)
        continue
    else:
        for k in range(len(n)):
            if n[k] == "<":
                j += 1
            else:
                j -= 1
            if j == 0:
                count = k+1
                if k != len(n)-1 and n[k+1] == ">":
                    break
        print(count)