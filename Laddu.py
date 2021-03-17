for contestant in range(int(input())):
    activities = input().split()
    act = int(activities[0])
    origin = activities[1]
    lad = 0
    for i in range(int(act)):
        a = input().split()
        if a[0] == "CONTEST_WON":
            if int(a[1])>20:
                lad = lad + 300
            else:
                lad = lad + 300 + (20 - int(a[1]))
        if a[0] == "BUG_FOUND":
            lad = lad + int(a[1])
        if a[0] == "TOP_CONTRIBUTOR":
            lad = lad + 300
        if a[0] == "CONTEST_HOSTED":
            lad = lad + 50
    if origin == "INDIAN":
        print(lad // 200)
    else:
        print(lad // 400)