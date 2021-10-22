
# 메모리 42312KB 시간 4780ms
import sys
N, M = sys.stdin.readline().split() # 3 4

h = [input() for _ in range(int(N))]
s = [input() for _ in range(int(M))]

h_and_s = set(h).intersection(set(s))
h_and_s = sorted(list(h_and_s))

print(len(h_and_s)) # 2
for i in h_and_s:
    print(i)
# baesangwook
# ohhenrie



# 메모리 41748KB 시간 136ms
import sys
N, M =  sys.stdin.readline().split()


h = set() # 듣도 못한 사람
s = set() # 보도 못한 사람

for _ in range(int(N)):
    h.add(sys.stdin.readline().strip())
for _ in range(int(M)):
    s.add(sys.stdin.readline().strip())

h_and_s = sorted(list(h & s))
print(len(h_and_s))
for i in h_and_s:
    print(i)
