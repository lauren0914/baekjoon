N = int(input()) # 2

for ban in range(1, N+1): # 1, 2
    num_list = list(map(int, input().split())) # 5 30 25 76 23 78

    num_list = num_list[1:] # 30 25 76 23 78
    num_list.sort(reverse=True) # 78, 76, 30, 25, 23

    max, min = num_list[0], num_list[0] # 78, 78

    for n in num_list: # 78
        if max < n:
            max = n
        if min > n:
            min = n

    max_gap = num_list[0] - num_list[1]
    for idx in range(len(num_list) - 1):
        gap = num_list[idx] - num_list[idx+1]

        if max_gap < gap:
            max_gap = gap

    print(f'Class {ban}')
    print(f'Max {max}, Min {min}, Largest gap {max_gap}')
