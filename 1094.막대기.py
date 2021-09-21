import sys
X = int(sys.stdin.readline())
stick = 64
count = 0
len = 0

while True:
    half = stick // 2 
    len += half 

    if len > X:
        len -= half 
        stick = half
        
    else:
        count += 1
        stick = half

    if len == X:
        break           
print(count)
        

x = int(input()) # 23
stick = [64, 32, 16, 8, 4, 2, 1]
count = 0
for s in stick:
    if x >= s :
     x -= s
     count += 1
print(count)