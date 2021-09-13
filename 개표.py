n = int(input())
v = input() # ABBABB

A_c, B_c = v.count('A'), v.count('B') 

if A_c > B_c :
    print('A')
elif B_c > A_c:
    print('B')
else:
    print('Tie')