def solve(r, n): # "", 53
    if n == 0: # n = 몫
        return r
    # 재귀 탈출
    
    # 순서에 유의!
    if n%2 == 1: 
        return solve("1"+r, n//2) # 1, 26/ 101, 6/ 10101, 1/ 110101, 0
    else:
        return solve("0"+r, n//2) # 01, 13/ 0101, 3

print(solve("", int(input())))
