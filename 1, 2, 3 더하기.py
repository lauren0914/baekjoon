def solve(n):
    if n == 1:
        return 1
    elif n == 2:
        return 2
    elif n == 3:
        return 4
    else:
        return solve(n-1) + solve(n-2) + solve(n-3) # solve(6) + solve(5) + solve(4)

T = int(input()) # 3

for _ in range(T): 
    n = int(input()) # 7
    print(solve(n))

