import sys

N = int(input()) # 3

for _ in range(N):
    x, y = map(int, sys.stdin.readline().split()) # 0 10
    count = 0
    for n in range(x, y+1):
        zero = str(n).count('0')
        count += zero
    print(count)
    

# 문자에 포함된 0의 개수를 찾는 문제이기 때문에. 
# 아래처럼 풀면 '1000'은 1개로 count 된다.   
# N = int(input())

# for _ in range(N):
#     x, y = map(int, input().split())
#     count = 0
#     for n in range(x, y+1):
#         if n % 10 == 0:
#             count += 1
#     print(count)