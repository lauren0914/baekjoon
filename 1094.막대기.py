# 풀이1. 시간초과
X = int(input())
stick = 64 
count = 0
len = 0  # X와 비교할 막대길이

while True:
    if X == 64:
        count += 1
        break

    half = stick // 2 # 32, 16, 8, 4, 2, 1
    stick = half 
    len += half # 16+8 =24, 16+4=20, 22, 23

    if len > X: # 32 > 23, 24 > 23
        len -= half # len=0, 16
        
    else : # 16 < 23, 20 < 23
        count += 1

    if len == X:
        break           
print(count)
        
# 풀이2
x = int(input()) # 23
stick = [64, 32, 16, 8, 4, 2, 1]
count = 0
for s in stick:
    if x >= s :
     x -= s # 7, 3
     count += 1 # 2
print(count)