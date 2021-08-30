def div(num_list):
  sosu = 0
  for num in num_list:
    error = 0
    if num > 1:
     for i in range(2, num):
       if num % i == 0:
         error += 1
     if error == 0:
       sosu += 1
  return sosu


N = int(input())
num_list = list(map(int, input().split())) # [1, 3, 5, 7]

print(div(num_list))
# 

def div(num_list):
  if 1 in num_list:
    num_list.remove(1)
    return div(num_list)


  for num in num_list:
    for i in range(2, num):
      if num % i == 0:
        num_list.remove(num)
        break
  return num_list

N = int(input())
num_list = list(map(int, input().split()))

print(len(div(num_list)))



