# N = int(input())

n_list = [5, 3, 2, 1, 4]
s_list = sorted(n_list)
# for _ in range(N):
#     n_list.append(int(input()))
# q = n_list[0]
# f = n_list[1]
# r = n_list[-1]


def sort_list(n_list, p, f_i, f, r_i, r):
    if n_list == s_list:
        return n_list
    while p > f:
        if f_i == len(n_list)-1:
            break
        f_i += 1
        print(f)

    while p < r:
        if r_i == 0:
            break
        r_i -= 1
        print(r)

    if f_i > r_i:
        n_list[0], n_list[r_i] = r, p
    else:
        n_list[f_i], n_list[r_i] = r, f

    return sort_list(n_list, p, f_i, f, r_i, r)

p = n_list[0]
f_i = 1
f = n_list[f_i]

r_i = -1
r = n_list[r_i]

print(sort_list(n_list, p, f_i, f, r_i, r))