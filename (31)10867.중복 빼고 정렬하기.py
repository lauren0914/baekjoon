import sys

N = int(sys.stdin.readline())
n_list = list(map(int, sys.stdin.readline().split()))
n_list = list(set(n_list))
n_list.sort()
print(*n_list)