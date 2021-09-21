def rev(string):
    string = string[::-1]
    return int(string)

x, y = input().split()
res = rev(str(rev(x) + rev(y)))

print(res)

# x, y = input().split()
# res = int(x) + int(y)
# res = str(res)
# print(res)

