for t in range(int(input())):
    n = int(input())
    sa = sb = ba = bb = 0
    s = input()
    for j in range(len(s)):
        if j%2 == 0:
            if s[j] == "0":
                bb = bb +1
            else:
                sb = sb +1
        else:
            if s[j] == "0":
                ba = ba +1
            else:
                sa = sa +1
        if sb+ba > n or sa+bb > n:
            break
    print(j+1)      
