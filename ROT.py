
s_list = list(input()) # One is 1

# ord('A') = 65, ord('Z') = 90
# ord('a') = 97, ord('z') = 122

for i in range(len(s_list)):
    if 65 <= ord(s_list[i]) <= 90:
        if ord(s_list[i]) + 13 > 90:
            s_list[i] = chr(ord(s_list[i]) - 13)
        else:
            s_list[i] = chr(ord(s_list[i]) + 13)

    elif 97 <= ord(s_list[i]) <= 122:
        if ord(s_list[i]) + 13 > 122:
            s_list[i] = chr(ord(s_list[i]) - 13)
        else:
            s_list[i] = chr(ord(s_list[i]) + 13)
print(*s_list, sep='') 
# print(*s_list, end='') 
    


