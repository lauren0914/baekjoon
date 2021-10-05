from collections import deque

test_case = int(input()) # 3
for _ in range(test_case):
    n, m = map(int, input().split()) # 문서의 개수, 출력순서를 확인할 문서의 위치 (4, 2(0부터 시작))
    queue = deque(map(int, input().split())) # 1 2 3 4 -> 3번 문서의 출력순서를 파악 

    count = 0  # 출력 횟수
    while queue:
        best = max(queue)       # 4
        front = queue.popleft() # 1
        m -= 1

        if best == front:
            count += 1
            if m < 0:   # 3 0 / 5, 1, 2
                break

        elif best > front:
            queue.append(front) # 2 3 4 1
            if m < 0:
                m = len(queue) - 1
    print(count)