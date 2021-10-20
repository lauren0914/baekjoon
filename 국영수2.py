import sys

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

score.sort(key=lambda x:x[0])
score.sort(key=lambda x:x[3], reverse=True)
score.sort(key=lambda x:x[2])
score.sort(key=lambda x:x[1], reverse=True)

for i in score:
    print(i[0])

    

N = int(sys.stdin.readline())
score = []
for _ in range(N):
    name, kor, eng, math = map(str, sys.stdin.readline().split())
    score.append([name, int(kor), int(eng), int(math)])

score.sort(key=lambda x:x[1], reverse=True)
for i in score:
    print(i)
print()
score.sort(key=lambda x:x[2])
for i in score:
    print(i)
print()
score.sort(key=lambda x:x[3], reverse=True)
for i in score:
    print(i)
print()
score.sort(key=lambda x:x[0])
for i in score:
    print(i[0])
print()

score.sort(key=lambda x:x[0])
for i in score:
    print(i)
print()
score.sort(key=lambda x:x[3], reverse=True)
for i in score:
    print(i)
print()
score.sort(key=lambda x:x[2])
for i in score:
    print(i)
print()
score.sort(key=lambda x:x[1], reverse=True)
for i in score:
    print(i)
print()
for i in score:
    print(i[0])
