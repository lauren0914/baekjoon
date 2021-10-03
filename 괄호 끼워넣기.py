# 풀이1)
S = list(input())
pop_list = S.copy()
s_list = []

for s in enumerate(S):
    if s == '(': 
        s_list.append('(')
        pop_list.remove('(')

    else: 
        if len(s_list) > 0: 
            s_list.pop()
            pop_list.remove(s) 
            
print(len(pop_list + s_list))

# index 로 접근하면 안 되는 이유
# list 배열이 계속 바뀌기 때문
# [1, 2, 3, 4] -> [1, 3, 4] 되었을 때
# 첫 번째 배열에서 3의 index=2, 두 번째 배열에서 3의 index=1
# range 로 도는 거였으면, 3은 index가 1로 바뀌면서 건너뛰게 됨


# 풀이2)
def stack(S,idx,pop_list,s_list):
    if idx >= len(S):
        return len(pop_list + s_list)

    if S[idx] == '(':
        s_list.append('(')
        pop_list.remove('(')

    else:
        if s_list:
            s_list.pop()
            pop_list.remove(')')
    return stack(S, idx+1, pop_list, s_list)

S = list(input())
s_list = []
pop_list = S.copy()
idx = 0
print(stack(S, idx, pop_list, s_list))


# 풀이3)

S = input() # )(()
close = 0 # 1
open = 0  # 1

for s in S:
    if s == '(':
        open += 1
    else:
        if open:
            open -= 1
        else:
            close += 1
print(close + open)

# 풀이4)
S = input() # )(()
stack = []

for s in S:
    if s == '(':
        stack.append(s)
    else:
        if stack and stack[-1] == '(':
            stack.pop()
        else:
            stack.append(s)
print(len(stack))


