from collections import deque

def parentheses_checker(string): # (())())
    stack = deque() # append, pop 빠름
    check = True    

    for i in range(len(string)):
        if string[i] == "(": # (())())
            stack.append(i)
        
        if string[i] == ")":
            if stack:
                stack.pop() # )
            else:
                check = False
    
    if check == False or stack:  # (( : True, stack 비어있지 않음, )) : False, stack 비어있음
        print("NO")
    else:
        print("YES")


T = int(input())

for _ in range(T):
    string = input()
    parentheses_checker(string)