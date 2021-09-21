import string
alphabet = list(string.ascii_lowercase)
string = ['m', 'o', 'b', 'i', 't', 'e', 'l'] # 7개. 5까지
# num_list = [12, 14, 1,  8,   19,  4,   11]

# for _ in string:
#     print(alphabet.index(_))


def split_string(alphabet, string, start, end):
    s_min_idx = alphabet.index(string[start])
    s_min = string[start]
    
    for idx in range(len(string)-2):
        if s_min_idx > alphabet.index(string[idx]):
            s_min_idx = alphabet.index(string[idx])
            s_min = string[idx]
            # start = 0
            end = idx
    list1.extend(string[end::-1]) # append를 하니까 [[]] 가 됨
    split_string(alphabet, string[end+1: len(string)-1], start, end)
    

print(split_string(alphabet, string, 0, len(string)-2))
print(list1)