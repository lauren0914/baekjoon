import sys

N = int(input())

for _ in range(N):
    x, y = map(int, sys.stdin.readline().split())
    count = 0
    for n in range(x, y+1):
        zero = str(n).count('0')
        count += zero
    print(count)
    
# N = int(input())

# for _ in range(N):
#     x, y = map(int, input().split())
#     count = 0
#     for n in range(x, y+1):
#         if n % 10 == 0:
#             count += 1
#     print(count)