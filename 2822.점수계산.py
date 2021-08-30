score_list = []
for _ in range(8):
  score_list.append(int(input()))  # [20, 30, 50, 80, 110, 11, 0, 85]

score_dict = {}
for idx, score in enumerate(score_list):
  score_dict[idx] = score
sort_score = sorted(score_dict.items(), key = lambda x : x[1], reverse=True)
# [(4, 110), (7, 85), (3, 80), (2, 50), (1, 30), (0, 20), (5, 11), (6, 0)]

sum = 0
num_5 = []
for i in range(5):
  sum += int(sort_score[i][1])
  num_5.append(int(sort_score[i][0]) + 1)
  # [5, 8, 4, 3, 2]
print(sum)

num_5.sort()
for n in num_5:
  print(n, end=' ')