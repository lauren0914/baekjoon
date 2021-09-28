N, K = map(int, input().split())
arr = [i for i in range(1, int(N)+1)]
result = []
num = K-1

for i in range(N):
    if len(arr) > num:
        result.append(arr.pop(num))
        num += K-1
    elif len(arr) < num:
        num = num % len(arr)
        result.append(arr.pop(num))
        num += K-1

            

