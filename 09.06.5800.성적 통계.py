N = int(input())

for ban in range(1, N+1):
    class_list = list(map(int, input().split()))
    class_list = class_list[1:]
    class_list.sort(reverse=True)

    max, min = class_list[0], class_list[0]

    for n in class_list:
        if max < n:
            max = n
        if min > n:
            min = n

    max_gap = class_list[0] - class_list[1]
    for idx in range(len(class_list) - 1):
        gap = class_list[idx] - class_list[idx+1]

        if max_gap < gap:
            max_gap = gap
    print(f'Class {ban}')
    print(f'Max {max}, Min {min}, Largest gap {max_gap}')
