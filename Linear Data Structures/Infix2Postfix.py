def fun(s):
    if s == "+" or s == "-":
        return 1
    elif s == "*" or s == "/":
        return 2
    elif s == "^":
        return 3
    return 0

T = int(input())
for i in range(T):
    N = int(input())
    S = input()
    stack = []
    op = ""
    for j in S:
        if j.isalpha():
            op = op + j
        elif j == "(":
            stack.append(j)
        elif j == ")":
            while stack and stack[-1] != "(":
                op = op + stack.pop()
            stack.pop()
        else:
            while stack and fun(j) <= fun(stack[-1]):
                op = op + stack.pop()
            stack.append(j)
    while stack != []:
        op += stack.pop()
    print(op)