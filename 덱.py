import sys
from collections import deque

N = int(sys.stdin.readline())
dq = deque()

for i in range(N):
    cmd = sys.stdin.readline().split() # ['push_back', '1']
    if cmd[0] == 'push_front': # dq 앞에 정수 추가
        dq.appendleft(cmd[1])

    elif cmd[0] == 'push_back': # dq 뒤에 정수 추가
        dq.append(cmd[1])

    elif cmd[0] == 'pop_front': # dq 앞에 있는 정수 제거 및 출력, dq가 비어있으면 -1 출력
        if len(dq) == 0:
            print(-1)
        else:
            print(dq.popleft())

    elif cmd[0] == 'pop_back': # dq 뒤에 있는 정수 제거 및 출력, dq가 비어있으면 -1 출력
        if len(dq) == 0:
            print(-1)
        else:
            print(dq.pop())

    elif cmd[0] == 'size': # dq에 들어있는 정수의 개수 출력
        print(len(dq))

    elif cmd[0] == 'empty': # dq가 비어있으면 1, 아니면 0 출력
        if len(dq) == 0:
            print(1)
        else:
            print(0)

    elif cmd[0] == 'front': # dq 앞에 있는 정수 출력, dq가 비어있으면 -1 출력
        if len(dq) == 0:
            print(-1)
        else:
            print(dq[0])

    elif cmd[0] == 'back': # dq 뒤에 있는 정수 출력, dq가 비어있으면 -1 출력
        if len(dq) == 0:
            print(-1)
        else:
            print(dq[-1])



# 함수로 구현
import sys
from collections import deque


def push_front(n):
    dq.appendleft(n)

def push_back(n):
    dq.append(n)

def pop_front():
    if dq :
        return dq.popleft()
    else:
        return -1

def  pop_back():
    if dq:
        return dq.pop()
    else:
        return -1

def size():
    return len(dq)

def empty():
    if dq:
        return 0
    else:
        return 1

def front():
    if dq:
        return dq[0]
    else:
        return -1

def back():
    if dq:
        return dq[-1]
    else:
        return -1

N = int(sys.stdin.readline())
dq = deque()

for _ in range(N):
    com = sys.stdin.readline().split()
    if com[0] == 'push_front':
        push_front(com[1])
    elif com[0] == 'push_back':
        push_back(com[1])
    elif com[0] == 'pop_front':
        print(pop_front())
    elif com[0] == 'pop_back':
        print(pop_back())
    elif com[0] == 'size':
        print(size())
    elif com[0] == 'empty':
        print(empty())
    elif com[0] == 'front':
        print(front())
    elif com[0] == 'back':
        print(back())