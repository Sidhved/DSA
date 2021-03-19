n = int(input())
from collections import deque


stack = deque()
l = []
l.append(0)
l1 = []
l2 = []
l2.append(0)
l3 = []
l3.append(0)
l4 = []
l4.append(0)

s = input().split()
j = 0
m2 = 0
m1 = 0
k = 0
for i in s:
    j = j+1

    if i == "1":
        stack.append("Y")
        if len(stack)>m2:
            m2 = len(stack)
            l1.append(j)

    else:
        stack.pop()
        if len(stack) == 0:
            l2.append(j-l3[k])
            l3.append(j)
            k = k+1

            if(l3[k] -l3[k-1])>m1:
                m1 = l3[k] - l3[k-1]
                l4.append(l3[k-1]+1)
    
s = l1[-1]
f = m2
t = max(l2)
fo = l4[-1]
print(f, s, t, fo)