'''
1. 국어 점수 내림차순
2. 영어 점수 오름차순
3. 수학 점수 내림차순
4. 이름 오름차순
'''

import sys

N = int(sys.stdin.readline())
score = []
for _ in range(N):
    name, kor, eng, math = map(str, sys.stdin.readline().split())
    score.append([name, int(kor), int(eng), int(math)])
score.sort(key=lambda x: (-x[1], x[2], -x[3], x[0]))
# x[1]이 같다면 x[2] 

for i in score:
    print(i[0])