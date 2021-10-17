import sys

N = int(input())
M = int(input())
num = list(map(int, sys.stdin.readline().split()))
num.sort()

count = 0
i, j = 0, len(num)-1

while i < j:
    if num[i] + num[j] == M:
        count += 1
        i += 1
        j -= 1
    elif num[i] + num[j] < M :
        i += 1
    else :
        j -= 1
print(count)

