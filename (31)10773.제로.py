import sys

N = int(sys.stdin.readline())
n_list = []
for _ in range(N):
    n = int(sys.stdin.readline())
    if n == 0:
        del n_list[-1]
    else:
        n_list.append(n)
print(sum(n_list))